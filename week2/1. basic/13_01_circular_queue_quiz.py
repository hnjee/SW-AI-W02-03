class circular_queue:
    def __init__(self, n):
        self.arr = [None for _ in range(n)]
        self.in_index = 0
        self.out_index = 0
        self.count = 0
        self.n = n

    def enque(self, data):
        if self.count >= self.n:   # if self.in_index == self.out_index 
            raise IndexError("큐가 꽉찼습니다.")
        self.arr[self.in_index] = data
        self.in_index = (self.in_index + 1) % self.n
        self.count += 1 

    def deque(self):
        if self.count == 0: # if self.in_index == self.out_index 
            raise IndexError("큐가 비었습니다.")
        val = self.arr[self.out_index]
        self.arr[self.out_index] = None #빼도 됨 
        self.out_index = (self.out_index + 1) % self.n
        self.count -= 1 
        return val
    
    def size(self):
        return self.count
    
q = circular_queue(5)
q.enque(1)
q.enque(2)
q.enque(3)
q.enque(4)
q.enque(5)
#q.enque(6)
q.deque()
q.deque()
q.deque()
#q.enque(5)
q.deque()
q.deque()
q.deque()

n = q.size()
