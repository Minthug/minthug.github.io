# Spring Batch

Spring Batch는 대용량 데이터를 효율적으로 처리하기 위한 배치 처리 프레임워크 입니다.

왜 사용하나?
1. 대용량 처리
- 메모리 효율적인 청크 단위 처리
- 수백만 건의 데이터도 안정적 처리

2. 안정성
- 트랜잭션 관리, 재시작/복구 기능
- Skip, Retry 정책으로 장애 허용

3. 모니터링
- 작업 진행상황, 성공/실패 이력 추적
- JobRepository를 통한 메타데이터 관리

4. 표준화
- 일관된 배치 처리 패턴 제공
- 스프링 생태계와의 완벽한 통합

## 핵심 구성요소 4가지
1. Job

2. Step

3. ItemReader

4. ItemWriter

## 배치처리와 실시간 처리 차이는?
배치 처리는 미리 준비된 데이터로 빠른 응답, 하지만 데이터가 실시간 최신이 아닐 수 있음
실시간 처리는 요청 시점에 데이터 생성로 최신 데이터 보장, 하지만 응답이 느릴 수 있음

배치 -> 실시간 검색 순위 (10분마다 미리 계산해서 저장)
실시간 -> 구글 검색 (검색할 때 마다 실시간으로 결과 생성)

## Chunk 기반 처리와 Tasklet 기반 처리의 차이는?
Tasklet:

전체 데이터를 한 번에 처리
개발자가 직접 모든 로직 구현
단순하지만 메모리 사용량 많음

Chunk:

데이터를 정해진 크기로 나누어 처리
Spring Batch가 자동으로 반복 처리
메모리 효율적, 트랜잭션도 청크 단위

# Q. 배치 작업 모니터링은 어떻게 하셨나요?
별도의 모니터링 시스템은 구현하지 않았고, 기본적인 로깅으로만 처리했습니다. 각 청크 처리 시마다 로그를 남겨서 '페이지 1 완료: 100명', '총 300명 중 280명 성공' 이런 식으로 콘솔에서 진행상황을 확인했습니다
다만 실무에서는 배치 작업 모니터링이 중요하다는 것을 알고 있어서, 다음에는 진행률 추적, 실패 알림, 대시보드 같은 모니터링 기능을 추가하고 싶습니다. Spring Batch를 사용한다면 JobRepository를 통해 작업 이력과 상태를 체계적으로 관리할 수 있다는 점도 학습했습니다

## 배치 모니터링 작업
1. 기본 로깅
```java
@Slf4j
public class BatchService {
    public void processBatch() {
        log.info("배치 작업 시작: 총 {}건", totalCount);
        log.info("진행률: {}/{} ({}%)", current, total, progress);
        log.info("배치 작업 완료: 성공 {}, 실패 {}", success, fail);
    }
}
```

2. 상태 추적 객체(실시간 진행률)
```java
@Component
public class BatchMonitor {
    private final ConcurrentHashMap<String, BatchStatus> statusMap = new ConcurrentHashMap<>();
    
    public void updateProgress(String jobId, int current, int total) {
        BatchStatus status = statusMap.get(jobId);
        status.setProgress(current, total);
    }
    
    @GetMapping("/batch/{jobId}/status")
    public BatchStatus getStatus(@PathVariable String jobId) {
        return statusMap.get(jobId);
    }
}
```

3. 매트릭 수집 (Micrometer + Prometheus)
```java
@Component
public class BatchMetrics {
    private final Counter successCounter = Counter.builder("batch.success").register(meterRegistry);
    private final Timer batchTimer = Timer.builder("batch.duration").register(meterRegistry);
    
    public void recordSuccess() {
        successCounter.increment();
    }
}
```

