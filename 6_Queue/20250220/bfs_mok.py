# BFS (breadth first search)

# 간선 정보: 1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
# 정점 개수 V = 7, 간선의 개수 E = 8 일 때,

'''
7 8
1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7  # 무향 그래프. 방향성이 없다.
'''


def bfs(start):
    # 시작 정점에서 인접한 정점을 인접 순서대로 모두 방문. 그 이후 그 방문한 정점들 마다의 인접 정점을 다시 한 번 인접 순서대로 모두 방문.
    # 즉, 경로를 발견한 순서대로 방문한다. 방문 순서를 queue 에 저장하면 된다.
    queue = [start]

    visited = [0] * (V + 1)  # 정점 재방문을 방지하기 위해 방문한 정점을 표시하는 list 를 만듦.
    visited[start] = 1

    while queue:  # 방문할 정점이 남아있지 않을 때까지 반복.
        current = queue.pop(0)  # 경로를 되돌아오는 개념이 아니기 때문에 바로 pop 을 해야 함.
        # 현재 정점을 그 정점에서 방문 가능한 모든 정점으로 바꿔줘야 하는데, 선입선출로 하려고 pop(0) 하는 것.
        # 이후, 방문 가능한 모든 정점을 queue 뒤에 붙여줌. 이를 통해 다음, 그 다음의 정점에도 pop(0) 할 수 있게 됨.
        # visited[current] = 1  # 방문 체크를 여기서 해도 되는데, 아래 반복 구문이 조금 더 도는 경우가 있음.
        # 하지만, 여기서 방문 체크를 해야만 하는 문제도 있기 때문에, BFS 구조를 좀 더 잘 이해하자.
        print(current, end=' ')

        for i in range(1, V + 1):
            if adj[current][i] == 1 and not visited[i]:  # 현재 방문 가능한(연결되어 있고, 방문하지 않은) 모든 정점을 queue 에 넣음.
                queue.append(i)
                visited[i] = 1


V, E = map(int, input().split())
edges = list(map(int, input().split()))

# 그래프 저장은 인접행렬로 진행.

adj = [[0] * (V + 1) for _ in range(V + 1)]

for i in range(0, E * 2, 2):
    # edges[i], edges[i + 1]이 서로 연결된 것.
    adj[edges[i]][edges[i + 1]] = 1
    adj[edges[i + 1]][edges[i]] = 1  # 무향그래프이므로 양방향 모두를 기재해야 한다.

# for row in adj:
#     print(row)  # 잘 받아졌는지 꼭 확인하기

bfs(5)


# DFS, BFS 의 차이점
# DFS 는 정답이 있냐 없냐를 묻는 경우에 더 효율적이다. backtracking 이 가능하기 때문.
# BFS 는 가장 빠른 답을 찾는 경우에 더 효율적이다.