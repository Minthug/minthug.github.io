ArrayList와 LinkedList 상세 메커니즘
1. ArrayList의 내부 구조와 동적 크기 조정
내부 구조 (쉬운 설명)
javapublic class ArrayList<E> {
    // 실제 데이터를 저장하는 배열
    private Object[] elementData;
    
    // 현재 저장된 데이터 개수
    private int size;
    
    // 기본 크기는 10
    private static final int DEFAULT_CAPACITY = 10;
}
아파트로 비유:
elementData = [데이터1][데이터2][데이터3][ ][ ][ ][ ][ ][ ][ ]
size = 3     (실제 사용 중인 방: 3개)
capacity = 10 (전체 방 개수: 10개)
동적 크기 조정 과정
1단계: 공간 부족 감지
java// 새로운 데이터 추가 시
public boolean add(E e) {
    ensureCapacityInternal(size + 1); // 공간 체크
    elementData[size++] = e;
    return true;
}
2단계: 새 배열 생성 (1.5배 확장)
javaprivate void grow(int minCapacity) {
    int oldCapacity = elementData.length;     // 현재 크기: 10
    int newCapacity = oldCapacity + (oldCapacity >> 1); // 10 + 5 = 15
    elementData = Arrays.copyOf(elementData, newCapacity);
}
3단계: 데이터 복사
기존 배열: [A][B][C][D][E][F][G][H][I][J] (용량 10, 가득참)
새 배열:   [A][B][C][D][E][F][G][H][I][J][ ][ ][ ][ ][ ] (용량 15)
실제 동작 예시
javaList<String> list = new ArrayList<>(); // 용량 10으로 시작

// 1~10번째 추가 → 빠름
for(int i = 1; i <= 10; i++) {
    list.add("데이터" + i); // O(1)
}

// 11번째 추가 → 확장 발생
list.add("데이터11"); // O(n) - 전체 복사!

// 12~15번째 추가 → 다시 빠름
for(int i = 12; i <= 15; i++) {
    list.add("데이터" + i); // O(1)
}

2. LinkedList에서 중간 삽입/삭제가 빠른 이유
LinkedList 내부 구조
javapublic class LinkedList<E> {
    Node<E> first; // 첫 번째 노드
    Node<E> last;  // 마지막 노드
    
    private static class Node<E> {
        E item;        // 실제 데이터
        Node<E> next;  // 다음 노드 주소
        Node<E> prev;  // 이전 노드 주소
    }
}
기차로 비유한 구조
[이전|데이터A|다음] ↔ [이전|데이터B|다음] ↔ [이전|데이터C|다음]
      노드1              노드2              노드3
중간 삽입이 빠른 이유
ArrayList의 중간 삽입 (느림)
원본: [A][B][C][D][E]
↓ 인덱스 2에 X 삽입
과정: [A][B][ ][C][D][E] → C,D,E를 모두 뒤로 밀어야 함
결과: [A][B][X][C][D][E]
LinkedList의 중간 삽입 (빠름)
원본: [A] ↔ [B] ↔ [C]
↓ B와 C 사이에 X 삽입
과정: [A] ↔ [B] ↔ [X] ↔ [C]  (포인터만 변경!)
실제 삽입 과정
java// 1. 새 노드 생성
Node<E> newNode = new Node<>(prevNode, element, nextNode);

// 2. 앞 노드의 next를 새 노드로
prevNode.next = newNode;

// 3. 뒤 노드의 prev를 새 노드로  
nextNode.prev = newNode;

// 끝! 다른 데이터는 전혀 건드리지 않음
삭제도 마찬가지로 빠름
java// 노드 삭제 (포인터만 변경)
prevNode.next = nodeToDelete.next;
nextNode.prev = nodeToDelete.prev;
nodeToDelete = null; // 메모리 해제