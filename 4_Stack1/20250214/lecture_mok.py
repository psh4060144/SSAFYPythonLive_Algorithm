# DFS: 그래프의 모든 정점을 순회하는 방법 중 하나.
# 길을 한 방향으로 찾아가다가, 길이 없으면 되돌아가서 다시 탐색하는 방법
# 되돌아가는 것이 핵심. 따라서 되돌아갈 수 있도록 지나온 경로를 stack 에 저장
# 현재 위치: 경로상 마지막 요소.

# 그래프를 저장할 때는 각 정점이 어떻게 연결되어 있나를 저장해야 한다.
# 어떻게 저장하느냐? 인접 정보를 list 를 이용해서 저장할 것.
# graph.png 에 대해서 list 를 만들어보면,
# list = [
#     [0, 0, 1, 1, 0, 0, 0, 0],
#     [0, 1, 0, 0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 1, 0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0]
# ]
# 로 나타낼 수 있다.

# 간선 정보(edge, node vertex): 1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7
# 정점 갯수: V , 간선 갯수: E
# 해당 간선을 보고 data 를 작성하면...
# '1 2 1 3 2 4 2 5 3 7 4 6 5 6 6 7'

V = 7
E = 8
data = list(map(int, input().split()))


# 그래프를 저장하기 위해 인접 행렬(or 인접 list)를 활용.
adj = [[0] * (V + 1) for _ in range(V + 1)]  # V 번 index 를 활용해야 하기 때문에 (V + 1) * (V + 1) 의 행렬 생성.

for i in range(0, E * 2, 2):
    a, b = data[i], data[i + 1]
    adj[a][b] = 1
    adj[b][a] = 1

for row in adj:
    print(row)


# 시작 정점(node)에서부터 방문하는 정점(node)을 순서대로 '출력' 하는 함수
def dfs(start):
    stack = [start]
    # 방문했던 정점에 재방문하지 않기 위해 (되돌아오는 것은 제외하고) 방문 표시를 함.
    visited = [0] * (V + 1)  # visited list 에서 index 가 정점 번호, value 가 방문여부(1 or 0)
    visited[start] = 1
    print(start, end=' ')
    # 현재 위치에서 갈 수 있는 길이 있으면 이동.
    while stack:
        current = stack[-1]
        # current 가 현재 위치 정점의 번호. 정점 연결 정보는 인접 행렬이 가지고 있음.
        # 해야하는 것: 현재 정점과 연결된 정점을 찾는 것.
        for i in range(1, V + 1):
            if adj[current][i] and not visited[i]:  # current 정점과 i 번 정점이 연결되어 있고 방문하지 않았다면 1, 아니라면 0.
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
        else:  # for 문을 도는 동안 break 가 실행되지 않음 == if 문을 만족하지 않음 == 길 없음.
            stack.pop()  # 현재 위치를 경로에서 제거.

dfs(1)