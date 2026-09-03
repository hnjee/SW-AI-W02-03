"""
큐 (Queue) 구현
규칙: FIFO (First In, First Out) - 먼저 넣은 게 먼저 나온다

이번엔 두 단계로 진행합니다:
1) 리스트로 구현 (쉬움, 그런데 성능 문제가 있음)
2) collections.deque로 구현 (왜 이게 더 나은지 체감하기)
"""

from collections import deque
import time

# ==========================================
# 1단계: 리스트 기반 큐
# ==========================================
class QueueWithList:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """큐 뒤에 원소를 추가한다."""
        self._data.append(item)

    def dequeue(self):
        """큐 앞의 원소를 꺼내서 반환한다. 비어있으면 예외 처리."""
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self._data.pop(0) #비효율적!
        
    def peek(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self._data[0]

    def is_empty(self):
        return not len(self._data)

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"QueueWithList({self._data})"


# ==========================================
# 2단계: deque 기반 큐
# ==========================================
class QueueWithDeque:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """큐 뒤에 원소를 추가한다."""
        self._data.append(item)

    def dequeue(self):
        """큐 앞의 원소를 꺼내서 반환한다."""
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self._data[0]
        
    def is_empty(self):
        return not len(self._data)

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"QueueWithDeque({list(self._data)})"


# ----------------------------------------
# 테스트 코드
# ----------------------------------------
if __name__ == "__main__":
    print("=== QueueWithList 테스트 ===")
    q = QueueWithList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)  # QueueWithList([1, 2, 3])
    print("dequeue:", q.dequeue())  # 1 (먼저 넣은 게 먼저 나옴!)
    print(q)  # QueueWithList([2, 3])

    print()
    print("=== QueueWithDeque 테스트 ===")
    q2 = QueueWithDeque()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    print(q2)
    print("dequeue:", q2.dequeue())
    print(q2)


# ----------------------------------------
# 실험: 왜 리스트의 pop(0)이 느릴까?
# ----------------------------------------
# 아래 실험을 직접 실행해서 두 방식의 시간 차이를 눈으로 확인해보세요.
# (구현을 다 마친 후에 실행하세요!)

def benchmark():
    n = 50000

    # 리스트 버전
    q1 = QueueWithList()
    for i in range(n):
        q1.enqueue(i)

    start = time.time()
    for _ in range(n):
        q1.dequeue()
    list_time = time.time() - start

    # deque 버전
    q2 = QueueWithDeque()
    for i in range(n):
        q2.enqueue(i)

    start = time.time()
    for _ in range(n):
        q2.dequeue()
    deque_time = time.time() - start

    print(f"\n원소 {n}개 dequeue 시간 비교:")
    print(f"  리스트(pop(0)):     {list_time:.4f}초")
    print(f"  deque(popleft()):  {deque_time:.4f}초")
    print(f"  -> deque가 약 {list_time / deque_time:.1f}배 빠름")


benchmark()  # 구현 다 마친 후 이 줄의 주석을 풀고 실행해보세요!

