# @RequestBody VS @RequestParams VS @ModelAttribute

1. @RequestBody
JSON데이터를 객체로 변환
데이터 수정/생성 -> @RequestBody
POST   /api/users              # 사용자 생성 (JSON 데이터)
PUT    /api/users/123          # 사용자 수정 (JSON 데이터)

```java
{
  "name": "김철수",
  "email": "kim@example.com",
  "age": 30
}

@PostMapping("/users")
public ResponseEntity<User> createUser(@RequestBody UserCreateRequest request) {
    User user = userService.createUser(request);
    return ResponseEntity.ok(user);
}

// DTO
public class UserCreateRequest {
    private String name;
    private String email;
    private int age;
    
    // getters, setters
}
```

2. @RequestParams
URL 파라미터나 쿼리 스트링 받기
주로 검색/조회/페이징 -> @RequestParams
GET    /api/users?name=김철수&age=30&page=1    # 검색 조건
GET    /api/users?sort=name&order=asc          # 정렬 조건

```java
# GET /users?name=김철수&page=1&size=10
@GetMapping("/users")
public ResponseEntity<List<User>> getUsers(
    @RequestParam(required = false) String name,
    @RequestParam(defaultValue = "0") int page,
    @RequestParam(defaultValue = "10") int size
) {
    List<User> users = userService.findUsers(name, page, size);
    return ResponseEntity.ok(users);
}

# 실제 프로젝트에서 사용한 예시
@GetMapping("/figures")
public ResponseEntity<List<FigureDTO>> getFigures(
    @RequestParam(required = false) String keyword,
    @RequestParam(required = false) FigureParty party,
    @RequestParam(defaultValue = "0") int page
) {
    return ResponseEntity.ok(figureService.searchFigures(keyword, party, page));
}
```

3. @ModelAttribute
전통적인 HTML 폼 데이터 처리
파일 업로드 시에 가끔 사용합니다.

```java
# 요즘엔 거의 사용하지 않는 방식
@PostMapping("/users/form")
public String createUserForm(@ModelAttribute UserForm userForm, Model model) {
    userService.createUser(userForm);
    return "redirect:/users"; // 페이지 리다이렉트
}

# HTML 폼 (요즘엔 React, Vue 등 사용)
<form method="post" action="/users/form">
    <input name="name" type="text">
    <input name="email" type="email">
    <button type="submit">전송</button>
</form>
```

4. @PathVariable
URL 경로에서 값을 추출합니다.
특정 리소스 대상 -> @PathVariable
GET    /api/users/123           # 특정 사용자 조회
PUT    /api/users/123           # 특정 사용자 수정  
DELETE /api/users/123           # 특정 사용자 삭제
GET    /api/users/123/orders    # 특정 사용자의 주문 목록

```java
# 실제 프로젝트에서 가장 많이 사용하는 패턴
@GetMapping("/api/figures/{id}")
public ResponseEntity<FigureDTO> getFigure(@PathVariable String id) {
    FigureDTO figure = figureService.getFigure(id);
    return ResponseEntity.ok(figure);
}

@DeleteMapping("/api/figures/{id}")
public ResponseEntity<Void> deleteFigure(@PathVariable String id) {
    figureService.deleteFigure(id);
    return ResponseEntity.ok().build();
}

@PutMapping("/api/figures/{id}")
public ResponseEntity<FigureDTO> updateFigure(
    @PathVariable String id,
    @RequestBody UpdateFigureRequest request
) {
    FigureDTO figure = figureService.updateFigure(id, request);
    return ResponseEntity.ok(figure);
}

# 중첩 리소스도 자주 사용
@GetMapping("/api/figures/{figureId}/bills")
public ResponseEntity<List<BillDTO>> getFigureBills(@PathVariable String figureId) {
    List<BillDTO> bills = billService.getBillsByFigure(figureId);
    return ResponseEntity.ok(bills);
}
```

요약
@RequestBody는 JSON 데이터를 객체로 변환할 때 사용하고,
@RequestParams는 URL 파라미터나 쿼리 스트링을 받을 때 사용합니다

실제 프로젝트에서는 @PathVariable을 많이 사용했는데
GET/figure/{id} 같은 특정 리소스 조회나 DELETE~ 같은 리소스 삭제 시에 활용했습니다.

@RequestBody POST/PUT 데이터 생성/수정할 때, @RequestParams 검색이나 페이징에 사용했습니다.

### 꼬리 질문
Q: "언제 PathVariable을 사용하나요?"
→ A: "특정 리소스를 식별할 때 사용합니다. /users/123에서 123이 사용자 ID처럼 리소스를 특정할 수 있는 값일 때 PathVariable을 씁니다."
Q: "PathVariable과 RequestParam 차이는?"
→ A: "PathVariable은 필수값이고 URL 구조의 일부이며, RequestParam은 선택적이고 검색 조건 같은 부가 정보입니다."
Q: "RESTful API 설계 원칙은?"
→ A: "리소스는 PathVariable로, 동작은 HTTP 메소드로, 검색 조건은 RequestParam으로, 데이터는 RequestBody로 표현합니다."