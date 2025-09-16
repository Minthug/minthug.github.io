# Node 학습 정리

자바와 비교하면 쉽게 이해하기

## NPM (Node Package Manager)
- Java의 Maven/Gradle과 같은 패키지 관리 도구
- Node.js 설치 시 자동으로 함께 설치

- Maven의 pom.xml == NPM의 package.json
- Maven의 mvn install == NPM의 npm install
- node_modules 폴더가 라이브러리 저장소 역할

## ES6+ vs Java 차이
1. 변수 선언
```javascript
const name = "A"; // 상수 (Java의 final과 유사)
let age = 25; // 변수
var old = 30; // 구식 문법
```

```java
final String name = "A";
int age = 25;
```

2. 화살표 함수
```javascript
const add = (a, b) => a + b;
const users = [1,2,3].map(x => x * 2);
```

```java
Function<Integer, Integer> add = (a, b) -> a + b;
List<Integer> result = users.straem().map(x -> x * 2).collect(toList());
```

3. 비동기 처리
```javascript
const data = await fetch('/api/users');
```

```java
String data = httpClient.get("/api/users");
```

4. 타입
- Javascript: 동적 타입(런타입에 타입 결정)
- Java: 정적 타입(컴파일타입에 타입 결정)


## NestJS 스터디

Nest는 아래를 포함합니다
- OOP 객체지향 프로그래밍 
- FP Functional 프로그래밍
- FRP Functional React 프로그래밍

- Nest는 외부 모듈을 자유롭게 이용할 수 있습니다.
- Nest는 unit 테스트와 e2e 테스트를 할 수 있는 툴을 제공합니다.

### main.ts
프로젝트 시작점(entry point)

Module은 
Controller와 Provider로 구성

Client에 Request를 받아 Controller가 Provider에게 요청
Provider는 요청받은 내용을 처리해 Controller에게 다시 보내고
Response를 Controller가 Client에게 다시 전송

> MVC 패턴과 비슷한듯? Provider가 MV의 역할을 수행

## 소스 자동생성
- nest g module users
```javascript
import { Module } from '@nestjs/common';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

@Module({
  controllers: [UsersController],
  providers: [UsersService]
})
export class UsersModule {}

```
- nest g controller users
```javascript

import { Controller } from '@nestjs/common';

@Controller('users')
export class UsersController {}
```

- nest g service users
```javascript
import { Injectable } from '@nestjs/common';

@Injectable()
export class UsersService {}
```

Nest Controller의 역할

NestJS의 Controller는 Client의 Request(요청)을 받아 처리한 후 Response(응답)하는 역할

Client의 요청이 들어왔을 때 요청에 따라 처리할 Controller로 분기 처리하는 것을 Routing이라 한다.

```java
@RestController
@RequestMapping("/users")
public class UserController {
    
    @GetMapping("/{id}")           // 라우팅
    public User getUser(@PathVariable Long id) {
        return userService.findById(id);  // 요청 처리 후 응답
    }
}
```
NestJS:
```typescript
@Controller('users')
export class UsersController {
    
    @Get(':id')                    // 라우팅
    getUser(@Param('id') id: string) {
        return this.userService.findById(id);  // 요청 처리 후 응답
    }
}
```
완전히 동일한 역할:

```
@RestController = @Controller
@GetMapping = @Get
@RequestMapping = 클래스 레벨 경로 설정
Request → Controller → Service → Response 흐름 동일
```

라우팅도 동일:
```java
// Java
@RequestMapping("/api/v1/users")  // 경로 라우팅
```
```typescript
// NestJS  
@Controller('api/v1/users')       // 경로 라우팅
```
결론: Java Spring과 NestJS는 MVC 패턴이 완전히 동일합니다. 문법만 다르고 개념과 역할은 똑같아요!
NestJS는 Spring Boot의 Node.js 버전이라고 봐도 된다.
