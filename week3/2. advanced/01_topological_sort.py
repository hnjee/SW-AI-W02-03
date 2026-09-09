"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort_bfs(vertices, edges):
    result = []
    in_degree_dict = {} 
    graph = {}
    que = deque()

    # 인접 dict, 진입차수 dict 만들기 
    for i in range(vertices):
        graph[i] = []
        in_degree_dict[i] = 0
        
    for x, y in edges:
        graph[x].append(y) # 인접 dict 만들기 
        in_degree_dict[y] = in_degree_dict.get(y, 0) + 1 # 진입차수 만들기 

    # 진입차수 0인 노드 큐에 넣기 
    for node, in_degree in in_degree_dict.items():
        if in_degree == 0:
            que.append(node)
            result.append(node)

    while len(que) > 0:
        node = que.popleft()
        for adj in graph[node]:
            in_degree_dict[adj] = in_degree_dict[adj] - 1 # 인접 노드 차수 하나 지우기
            if in_degree_dict[adj] == 0: # 차수 0된 노드 큐에 넣기 
                que.append(adj)
                result.append(adj)

    if len(result) < vertices:
        raise ValueError("사이클이 존재합니다")

    return result

def topological_sort_dfs(vertices, edges):

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort_bfs(vertices, edges)
    print(f"수강 순서: {result}")
