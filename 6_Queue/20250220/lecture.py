# BFS (Breadth First Search)
# 탐색 시작점의 인접 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접 정점들을 차례로 방문하는 방식.
# 인접 정점들에 대해 모두 탐색한 후, 차례로 다시 그 다음 정점들을 탐색해야 하므로, 선입선출 형태의 자료구조인 queue 를 활용.

# DFS 는 갈퀴모양으로 탐색이 진행되지만, BFS 는 동심원 모양으로 탐색이 진행된다.
# 즉, BFS 는 최소 경로를 찾는 데 유리하다.

"""
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
"""


def bfs(start, V):  # 시작 정점 위치, 마지막 정점 V

    visited = [0] * (V + 1)         # visited 생성
    queue = []                      # queue 생성
    queue.append(start)             # 시작점 enqueue
    visited[start] = 1              # 시작점 enqueue 표시

    while queue:                    # queue 가 비워질 때까지 반복
        t = queue.pop(0)            # dequeue 해서 t에 저장      # pop()하면 queue 가 아니라 stack 이 되는 거고, 그렇게 되면 BFS 가 아니라 DFS 가 된다.
        print(t)                    # t 정점에 대한 처리

        for w in adj_l[t]:
            if visited == 0:        # t 에 인접한 정점 w 중, enqueue 되지 않은 정점이 있다면
                queue.append(w)     # enqueue
                visited[w] = 1      # enqueue 표시


# 인접 리스트 --------------------------
V, E = map(int, input().split())
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V + 1)]
for i in range(0, E * 2, 2):
    v1, v2 = arr[i], arr[i + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
# ------------------------------------

bfs(1, 7)