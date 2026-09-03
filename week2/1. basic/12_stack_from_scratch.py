"""
스택 (Stack) 구현 - 파이썬 리스트 기반
규칙: LIFO (Last In, First Out) - 마지막에 넣은 게 먼저 나온다
"""

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """스택 맨 위에 원소를 추가한다."""
        self._data.append(item)

    def pop(self):
        """스택 맨 위 원소를 꺼내서 반환한다. 비어있으면 예외 처리."""
        if self.is_empty():
            raise IndexError("스택이 비어있습니다")
        return self._data.pop()

    def peek(self):
        """맨 위 원소를 꺼내지 않고 확인만 한다."""
        if self.is_empty():
            raise IndexError("스택이 비어있습니다")
        return self._data[-1]

    def is_empty(self):
        """스택이 비어있는지 확인한다."""
        return len(self._data)==0
    
    def size(self):
        """스택에 들어있는 원소 개수를 반환한다."""
        return len(self._data)
    
    def __repr__(self):
        return f"Stack({self._data})"


# ----------------------------------------
# 테스트 코드 (구현 후 실행해서 확인해보세요)
# ----------------------------------------
if __name__ == "__main__":
    s = Stack()
    print("비어있나?", s.is_empty())  # True
    s.peek()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s)  # Stack([1, 2, 3])
    print("크기:", s.size())  # 3

    print("peek:", s.peek())  # 3 (꺼내지진 않음)
    print("pop:", s.pop())    # 3
    print(s)  # Stack([1, 2])

    print("비어있나?", s.is_empty())  # False

