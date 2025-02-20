# maze


def find_start(arr):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(i, j, N):  # 시작 index i, j, 크기 N
    visited = [[0] * N for _ in range(N)]   # visited 생성
    queue = []                              # queue 생성
    queue.append([i, j])                    # 시작점 enqueue
    visited[i][j] = 1                       # 시작점 enqueue 표시
    while queue:                            # queue 에 남은 칸이 없을때까지 반복
        ti, tj = queue.pop(0)               # t <- dequeue
        if maze[ti][tj] == 3:
            return visited[ti][tj] - 2      # t에서 해야 할 일 수행. 출구(3)에 도착하면 1, 아니면 0 return.
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # t 에 인접한 w 중, enqueue 하지 않은 곳이면
            wi, wj = ti + di, tj + dj       # enqueue, 표시.
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
    return 0



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    sti, stj = find_start(N)

    ans = bfs(sti, stj, N)