1. 컬렉션 프레임워크란?
데이터를 저장하고 관리하기 위한 Java의 표준 라이브러리입니다. 배열의 한계를 극복하고 다양한 데이터 구조를 제공합니다.
배열의 한계
java// 배열의 문제점
String[] names = new String[5];  // 크기 고정
names[0] = "김철수";
names[1] = "이영희";
// names[5] = "박민수";  // 에러! 크기 초과
컬렉션의 장점
java// 컬렉션의 해결책
List<String> names = new ArrayList<>();  // 동적 크기
names.add("김철수");
names.add("이영희");
names.add("박민수");  // 자동으로 크기 확장!

2. 컬렉션 프레임워크 전체 구조도
최상위 구조
Iterable<T> (인터페이스)
    ↓
Collection<E> (인터페이스)
    ├── List<E>
    ├── Set<E>
    └── Queue<E>

Map<K,V> (별도 인터페이스 - Collection 상속 안함)
상세 계층 구조
Iterable<T>
    ↓
Collection<E>
    ├── List<E> (순서O, 중복O)
    │   ├── ArrayList
    │   ├── LinkedList
    │   └── Vector
    │
    ├── Set<E> (순서?, 중복X)
    │   ├── HashSet (순서X)
    │   ├── LinkedHashSet (삽입순서O)
    │   └── TreeSet (정렬순서O)
    │
    └── Queue<E> (FIFO)
        ├── LinkedList
        ├── PriorityQueue
        └── ArrayDeque

Map<K,V> (키-값 쌍)
    ├── HashMap
    ├── LinkedHashMap
    ├── TreeMap
    └── ConcurrentHashMap

3. 주요 인터페이스들과 특징
Iterable<T> 인터페이스
javapublic interface Iterable<T> {
    Iterator<T> iterator();  // 반복자 제공
}

// 사용 예시
for(String name : names) {  // Enhanced for-loop 가능
    System.out.println(name);
}
Collection<E> 인터페이스
javapublic interface Collection<E> extends Iterable<E> {
    boolean add(E e);           // 요소 추가
    boolean remove(Object o);   // 요소 제거
    int size();                 // 크기 반환
    boolean isEmpty();          // 비어있는지 확인
    boolean contains(Object o); // 포함 여부 확인
    void clear();              // 모든 요소 제거
}
List<E> 인터페이스
javapublic interface List<E> extends Collection<E> {
    E get(int index);              // 인덱스로 조회
    E set(int index, E element);   // 인덱스로 수정
    void add(int index, E element); // 특정 위치에 삽입
    E remove(int index);           // 인덱스로 삭제
}

// 특징: 순서가 있고, 중복 허용, 인덱스 접근 가능
List<String> fruits = new ArrayList<>();
fruits.add("사과");     // 0번 인덱스
fruits.add("바나나");   // 1번 인덱스
fruits.add("사과");     // 2번 인덱스 (중복 허용!)
Set<E> 인터페이스
javapublic interface Set<E> extends Collection<E> {
    // Collection의 메서드만 사용 (새로운 메서드 없음)
}

// 특징: 중복 불허, 순서는 구현체에 따라 다름
Set<String> fruits = new HashSet<>();
fruits.add("사과");
fruits.add("바나나");
fruits.add("사과");    // 중복! 추가되지 않음
System.out.println(fruits.size()); // 2 (사과, 바나나만)
Queue<E> 인터페이스
javapublic interface Queue<E> extends Collection<E> {
    boolean offer(E e);  // 요소 추가 (add와 유사)
    E poll();           // 요소 제거하고 반환 (없으면 null)
    E peek();           // 요소 확인 (제거하지 않음)
}

// 특징: FIFO (First In, First Out)
Queue<String> queue = new LinkedList<>();
queue.offer("첫번째");
queue.offer("두번째");
String first = queue.poll(); // "첫번째" 반환
Map<K,V> 인터페이스
javapublic interface Map<K,V> {
    V put(K key, V value);    // 키-값 저장
    V get(Object key);        // 키로 값 조회
    V remove(Object key);     // 키로 삭제
    boolean containsKey(Object key);  // 키 존재 여부
    Set<K> keySet();         // 모든 키 반환
    Collection<V> values();   // 모든 값 반환
}

// 특징: 키-값 쌍, 키는 중복 불허
Map<String, Integer> ages = new HashMap<>();
ages.put("김철수", 25);
ages.put("이영희", 30);
ages.put("김철수", 26);  // 기존 값 덮어씀
System.out.println(ages.get("김철수")); // 26