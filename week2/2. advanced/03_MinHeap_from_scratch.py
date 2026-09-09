class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return i * 2 + 1
    
    def _right(self, i):
        return i * 2 + 2 

    def push(self, value):
        # 끝에 추가 + sift up
        current_index = len(self.heap)
        self.heap.append(value)
        while current_index > 0:
            parent_index = self._parent(current_index)
            if self.heap[current_index] < self.heap[parent_index]:
                self.heap[parent_index], self.heap[current_index] = self.heap[current_index], self.heap[parent_index]
                current_index = parent_index
            else: 
                break

    def pop(self): 
        # 루트 꺼내기 + 끝 원소를 루트로 + sift down
        result = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
        current_index = 0
        while current_index < len(self.heap):
            left_index = self._left(current_index) 
            if left_index >= len(self.heap):
                break

            right_index = self._right(current_index)
            if right_index >= len(self.heap):
                min_index = left_index
            else: 
                min_index = left_index if self.heap[left_index] <= self.heap[right_index] else right_index

            if self.heap[current_index] > self.heap[min_index]:
                self.heap[current_index], self.heap[min_index] = self.heap[min_index], self.heap[current_index]
                current_index = min_index
            else:
                break
        return result
       
    def peek(self): 
        # 루트만 확인 (꺼내지 않고)
        return self.heap[0]

    def is_empty(self): 
        return len(self.heap) == 0

h = MinHeap()
for v in [5, 3, 8, 1, 9, 2]:
    h.push(v)

print(h.heap)  # 힙 배열 내부 상태 확인

result = []
while not h.is_empty():
    result.append(h.pop())

print(result)  # 오름차순으로 나오는지 확인: [1, 2, 3, 5, 8, 9]