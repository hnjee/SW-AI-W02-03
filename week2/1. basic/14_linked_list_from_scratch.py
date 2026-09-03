"""
연결리스트 (Linked List) 구현 - 단일 연결리스트 (Singly Linked List)

핵심 개념: 각 노드가 "다음 노드"에 대한 참조(포인터)를 가지고 있어요.
리스트처럼 연속된 메모리가 아니라, 노드들이 화살표로 이어진 형태예요.

    [head] -> [1|next] -> [2|next] -> [3|next] -> None

TODO 부분을 직접 채워보세요!
"""


class Node:
    """연결리스트의 한 칸(노드). 값(data)과 다음 노드에 대한 참조(next)를 가짐."""
    def __init__(self, data):
        self.data = data
        self.next = None  # 처음엔 다음 노드가 없으니 None

class LinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드를 가리킴 (비어있으면 None)
        self._size = 0

    def append(self, data):
        """리스트 맨 끝에 새 노드를 추가한다."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else: 
            node = self.head
            while node.next != None:
                node = node.next
            node.next = new_node

        self._size += 1

    def prepend(self, data):
        """리스트 맨 앞에 새 노드를 추가한다."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1


    def delete(self, data):
        """값이 data인 첫 번째 노드를 삭제한다. 없으면 아무 일도 안 함."""
        current_node = self.head
        if current_node is None: #빈 연결 리스트 -> return 
            return False
        if current_node.data == data: #첫 노드를 삭제해야하는 경우 -> self.head 변경 
            self.head = current_node.next
            self._size -= 1
            return True
        
        pre_node = current_node
        current_node = current_node.next
        while current_node is not None:
            if current_node.data == data:
                pre_node.next = current_node.next
                self._size -= 1
                return True
            pre_node = current_node
            current_node = current_node.next
        return False


    def find(self, data):
        """값이 data인 노드가 있으면 True, 없으면 False."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next 
        return False

    def to_list(self):
        """연결리스트의 내용을 파이썬 리스트로 변환 (테스트/출력용)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def size(self):
        return self._size

    def is_empty(self):
        return self.head is None

    def __repr__(self):
        return f"LinkedList({self.to_list()})"


# ----------------------------------------
# 테스트 코드
# ----------------------------------------
if __name__ == "__main__":
    ll = LinkedList()
    print("비어있나?", ll.is_empty())  # True

    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(ll)  # LinkedList([1, 2, 3])

    ll.prepend(0)
    print(ll)  # LinkedList([0, 1, 2, 3])

    print("find(2):", ll.find(2))  # True
    print("find(99):", ll.find(99))  # False

    ll.delete(2)
    print(ll)  # LinkedList([0, 1, 3])

    ll.delete(0)  # head 삭제 케이스
    print(ll)  # LinkedList([1, 3])

    print("size:", ll.size())  # 2


# ----------------------------------------
# 연습 문제 1: 연결리스트 뒤집기 (Reverse)
# ----------------------------------------
# 연결리스트의 방향을 통째로 뒤집는 메서드를 만들어보세요.
# 예: 1 -> 2 -> 3 -> None  이었던 것을  3 -> 2 -> 1 -> None 으로 바꾸기
#
# 힌트: 새 리스트를 만드는 게 아니라, 각 노드의 next 화살표 방향을
#       거꾸로 바꿔주는 것입니다. prev, current, next_node 세 개의
#       변수를 이용해서 한 칸씩 이동하면서 화살표를 뒤집어보세요.
#
# def reverse(self):
#     prev = None
#     current = self.head
#     while current:
#         next_node = current.next   # 다음 노드를 잃어버리지 않게 미리 저장
#         current.next = prev        # 화살표 방향을 거꾸로!
#         prev = current              # prev를 한 칸 전진
#         current = next_node         # current를 한 칸 전진
#     self.head = prev                # 마지막엔 prev가 새로운 head


# ----------------------------------------
# 연습 문제 2: 사이클(순환) 탐지 - Floyd's Cycle Detection
# ----------------------------------------
# 연결리스트 중간에 어떤 노드가 이전 노드를 다시 가리켜서 "원형"이 되어버린
# 경우를 탐지하는 함수를 만들어보세요. (일명 "토끼와 거북이" 알고리즘)
#
# 힌트: 느린 포인터(한 칸씩 이동)와 빠른 포인터(두 칸씩 이동)를 동시에
#       움직이세요. 사이클이 있다면 언젠가 두 포인터가 같은 노드에서 만나고,
#       사이클이 없다면 빠른 포인터가 None에 먼저 도달합니다.

def has_cycle(head):
    # TODO: 도전해보세요! (일단 위 문제 1을 먼저 풀어보시는 걸 추천)
    pass