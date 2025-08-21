# JWT Stateless + 권한 변경 대처

```
클라이언트 ←--JWT 토큰--→ 서버
           (서버는 상태 저장 안함)
```
JWT 토큰 안에 사용자 정보와 권한이 모두 들어있어서, 서버는 토큰만 검증하면 됨 (별도 세션 저장소 불필요)

```
// JWT 토큰 내용 예시
{
  "userId": 123,
  "username": "john",
  "roles": ["USER", "ADMIN"],  // 권한 정보
  "exp": 1640995200  // 만료시간
}
```

### 문제 상황: 권한 변경이 즉시 반영 안됨
시나리오:
1. 사용자가 JWT 토큰을 받음 (권한: ADMIN)
2. 관리자가 해당 사용자의 권한을 USER로 변경
3. 하지만 JWT 토큰은 여전히 ADMIN 권한을 가지고 있음!
4. 토큰이 만료될 때까지 계속 ADMIN으로 동작

```java
// 문제 상황
@RestController
public class AdminController {
    
    @GetMapping("/admin/users")
    @PreAuthorize("hasRole('ADMIN')")  // JWT에서 권한 확인
    public List<User> getUsers(HttpServletRequest request) {
        // JWT 토큰에 ADMIN이 있으면 통과
        // 실제 DB에서는 권한이 변경되었지만 반영 안됨!
        return userService.getAllUsers();
    }
}
```
## 해결 방법

### 1. 토큰 만료시간을 짧게 설정 + 자주 갱신

```java
// JWT 생성 시 짧은 만료시간 설정
public String generateToken(User user) {
    return Jwts.builder()
        .setSubject(user.getUsername())
        .claim("roles", user.getRoles())
        .setExpiration(new Date(System.currentTimeMillis() + 300000))  // 5분
        .signWith(secretKey)
        .compact();
}

// 리프레시 토큰으로 자주 갱신
@PostMapping("/refresh")
public ResponseEntity<String> refreshToken(@RequestBody RefreshRequest request) {
    // 최신 권한 정보로 새 토큰 발급
    User user = userService.findById(request.getUserId());
    String newToken = jwtService.generateToken(user);  // 최신 권한 반영
    return ResponseEntity.ok(newToken);
}
```

## 2. 블랙리스트 방식 (Redis 활용)
```java
@Service
public class TokenBlacklistService {
    
    @Autowired
    private RedisTemplate<String, String> redisTemplate;
    
    // 권한 변경 시 기존 토큰을 블랙리스트에 추가
    public void blacklistToken(String token) {
        String jti = extractJti(token);  // 토큰 고유 ID
        long expiration = extractExpiration(token);
        
        // Redis에 블랙리스트 저장 (만료시간까지)
        redisTemplate.opsForValue().set(
            "blacklist:" + jti, 
            "true", 
            Duration.ofMillis(expiration - System.currentTimeMillis())
        );
    }
    
    // 토큰 검증 시 블랙리스트 확인
    public boolean isBlacklisted(String token) {
        String jti = extractJti(token);
        return redisTemplate.hasKey("blacklist:" + jti);
    }
}

// JWT 필터에서 블랙리스트 확인
@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    
    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                  HttpServletResponse response, 
                                  FilterChain filterChain) {
        String token = extractToken(request);
        
        if (token != null && jwtService.isValidToken(token)) {
            // 블랙리스트 확인 추가!
            if (tokenBlacklistService.isBlacklisted(token)) {
                response.setStatus(HttpStatus.UNAUTHORIZED.value());
                return;
            }
            
            // 정상 처리
            Authentication auth = getAuthentication(token);
            SecurityContextHolder.getContext().setAuthentication(auth);
        }
        
        filterChain.doFilter(request, response);
    }
}
```

## 3. 중요한 작업 시 실시간 권한 확인
```java
@RestController
public class CriticalController {
    
    @DeleteMapping("/admin/users/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<String> deleteUser(@PathVariable Long id, 
                                           HttpServletRequest request) {
        String token = extractToken(request);
        Long userId = extractUserId(token);
        
        // 중요한 작업이므로 DB에서 실시간 권한 재확인!
        User currentUser = userService.findById(userId);
        if (!currentUser.hasRole("ADMIN")) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN)
                .body("권한이 변경되었습니다. 다시 로그인해주세요.");
        }
        
        // 권한 확인 후 실행
        userService.deleteUser(id);
        return ResponseEntity.ok("삭제 완료");
    }
}
```

## 4. 이벤트 기반 토큰 무효화
```java
// 권한 변경 시 이벤트 발행
@Service
public class UserService {
    
    @EventListener
    public void updateUserRole(Long userId, String newRole) {
        User user = userRepository.findById(userId);
        user.setRole(newRole);
        userRepository.save(user);
        
        // 이벤트 발행
        eventPublisher.publishEvent(new UserRoleChangedEvent(userId));
    }
}

// 이벤트 처리
@EventListener
public void onUserRoleChanged(UserRoleChangedEvent event) {
    // 해당 사용자의 모든 활성 토큰 무효화
    List<String> userTokens = findActiveTokensByUserId(event.getUserId());
    userTokens.forEach(token -> tokenBlacklistService.blacklistToken(token));
    
    // 클라이언트에게 재로그인 알림 (WebSocket 등)
    notificationService.notifyRelogin(event.getUserId());
}
```