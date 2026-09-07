"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False

힌트:
- target < root.value → 왼쪽으로 이동
- target > root.value → 오른쪽으로 이동
- target == root.value → 찾음!
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, target):
        node = self.root
        while node is not None:
            if node.value == target:
                return True
            elif node.value > target:
                node = node.left 
            else:
                node = node.right
        return False

        
    def insert(self, target):
        target_node = TreeNode(target)
        if self.root is None:
            self.root = target_node
            return

        node = self.root
        while node is not None:
            if node.value == target: #일단 값이 같은 건 안넣음 
                return 
            elif node.value > target:
                if node.left is None:
                    node.left = target_node
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = target_node
                    return 
                node = node.right


    def _get_min_node(self, root):
        node = root 
        while node is not None:
            if node.left is None:
                return node
            node = node.left
        return node 
    
    def _delete_recursive(self, node, target):
        if node is None: #끝까지 target 발견 못함 
            raise ValueError("트리에 해당 요소가 없습니다")
        
        if target < node.value: 
            node.left = self._delete_recursive(node.left, target)
        elif target > node.value:
            node.right = self._delete_recursive(node.right, target)
        else: #target 발견 -> 삭제
            # case 1. 자식 노드가 0~1개인 노드 지우기
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # case 2. 자식 노드가 2개인 노드 지우기 -> 이 노드 자리에 있어야하는 새로운 후보 찾기 
            else: 
                successor = self._get_min_node(node.right)
                print(successor.value)
                node.value = successor.value
                node.right = self._delete_recursive(node.right, successor.value)

        return node

    def delete(self, target):
        self.root = self._delete_recursive(self.root, target)
    
def insert_bst(root, target):
    target_node = TreeNode(target)
    if root is None:
        return 
    node = root 
    while node is not None:
        if node.value == target: #일단 값이 같은 건 안넣음 
            return 
        elif node.value > target:
            if node.left is None:
                node.left = target_node
                return
            node = node.left
        else:
            if node.right is None:
                node.right = target_node
                return 
            node = node.right
    

# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    bst = BST()
    bst.root = TreeNode(5)
    bst.root.left = TreeNode(3)
    bst.root.right = TreeNode(7)
    bst.root.left.left = TreeNode(2)
    bst.root.left.right = TreeNode(4)

    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")

    bst.insert(0)
    bst.delete(3)
    bst.delete(10)

    test_values = [2, 4, 5, 6, 3, 0]
    for val in test_values:
        result = bst.search(val)
        print(f"값 {val} 검색: {result}")

