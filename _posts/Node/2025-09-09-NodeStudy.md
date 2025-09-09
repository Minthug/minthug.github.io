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
