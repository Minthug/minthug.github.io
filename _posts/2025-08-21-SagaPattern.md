# Saga 패턴

## 1. Orchestration (중앙 관리)
```
            [Saga Orchestrator]
                 |
    ┌─────────────┼─────────────┐
    ↓             ↓             ↓
[주문서비스]   [결제서비스]   [재고서비스]   [배송서비스]
```

실제 동작 과정
```java
// Saga Orchestrator 의사코드
public class OrderSaga {
    
    public void processOrder(OrderRequest request) {
        try {
            // 1단계: 주문 생성
            Order order = orderService.createOrder(request);
            
            // 2단계: 결제 처리
            Payment payment = paymentService.processPayment(order);
            
            // 3단계: 재고 차감
            Stock stock = stockService.reduceStock(order);
            
            // 4단계: 배송 요청
            Shipping shipping = shippingService.requestShipping(order);
            
            // 모든 단계 성공!
            
        } catch (PaymentFailedException e) {
            // 결제 실패 시: 주문만 취소
            orderService.cancelOrder(order.getId());
            
        } catch (StockInsufficientException e) {
            // 재고 부족 시: 결제 취소 → 주문 취소
            paymentService.refund(payment.getId());
            orderService.cancelOrder(order.getId());
            
        } catch (ShippingFailedException e) {
            // 배송 실패 시: 재고 복구 → 결제 취소 → 주문 취소
            stockService.restoreStock(stock.getId());
            paymentService.refund(payment.getId());
            orderService.cancelOrder(order.getId());
        }
    }
}
```

## 2. Compensating Transaction (보상 작업)
보상 작업이란?
이미 성공한 작업을 "되돌리는 작업"

**실제로는 데이터를 삭제하지 않고, 상태를 변경하는 방식**

```java
// 주문 서비스
class OrderService {
    // 정상 작업
    public Order createOrder(OrderRequest request) {
        Order order = new Order(request);
        order.setStatus("CREATED");  // 상태: 생성됨
        return orderRepository.save(order);
    }
    
    // 보상 작업
    public void cancelOrder(Long orderId) {
        Order order = orderRepository.findById(orderId);
        order.setStatus("CANCELLED");  // 상태만 변경 (삭제 X)
        orderRepository.save(order);
    }
}

// 결제 서비스  
class PaymentService {
    // 정상 작업
    public Payment processPayment(Order order) {
        Payment payment = new Payment(order);
        payment.setStatus("COMPLETED");  // 결제 완료
        // 실제 카드사 API 호출
        return paymentRepository.save(payment);
    }
    
    // 보상 작업
    public void refund(Long paymentId) {
        Payment payment = paymentRepository.findById(paymentId);
        payment.setStatus("REFUNDED");  // 환불 상태로 변경
        // 실제 환불 API 호출
        paymentRepository.save(payment);
    }
}

// 재고 서비스
class StockService {
    // 정상 작업
    public Stock reduceStock(Order order) {
        Stock stock = stockRepository.findByProductId(order.getProductId());
        stock.setQuantity(stock.getQuantity() - order.getQuantity());
        return stockRepository.save(stock);
    }
    
    // 보상 작업
    public void restoreStock(Long stockId) {
        Stock stock = stockRepository.findById(stockId);
        stock.setQuantity(stock.getQuantity() + order.getQuantity());  // 수량 복구
        stockRepository.save(stock);
    }
}
```

## 3. Choreography 방식 (이벤트 기반)
```
주문서비스 --OrderCreated--> 결제서비스 --PaymentCompleted--> 재고서비스
    ↑                                                              |
    └--------StockReduced 이벤트 ← 배송서비스 ←--StockReduced------┘
```

```java
// 주문 서비스
@EventListener
public void onOrderCreated(OrderCreatedEvent event) {
    // 결제 서비스에 이벤트 발행
    eventPublisher.publish(new PaymentRequestEvent(event.getOrderId()));
}

// 결제 서비스  
@EventListener
public void onPaymentRequest(PaymentRequestEvent event) {
    try {
        processPayment(event.getOrderId());
        // 성공 시 다음 단계로
        eventPublisher.publish(new PaymentCompletedEvent(event.getOrderId()));
    } catch (Exception e) {
        // 실패 시 보상 이벤트
        eventPublisher.publish(new PaymentFailedEvent(event.getOrderId()));
    }
}

// 주문 서비스가 실패 이벤트 수신
@EventListener  
public void onPaymentFailed(PaymentFailedEvent event) {
    cancelOrder(event.getOrderId());  // 보상 작업 실행
}
```
핵심 정리
Saga 패턴 = 각자 일하고, 실패하면 이전 일들을 차례로 되돌리기

정상 흐름: A → B → C → D (순차 실행)
실패 시: C에서 실패 → B 되돌리기 → A 되돌리기

보상 작업의 핵심:

실제 삭제가 아닌 상태 변경
순서가 중요 (역순으로 되돌려야 함)
각 보상 작업은 실패하면 안 됨 (멱등성 보장)

