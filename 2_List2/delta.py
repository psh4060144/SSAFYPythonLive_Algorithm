# 델타
# 2차 배열의 한 좌표에서 네 방향(상하좌우)의 인접 배열 요소를 탐색하는 방법.
# index (i,j)인 칸의 상하좌우 칸 (ni,nj)
'''
       |  j - 1  |     j     |  j + 1
i - 1  |    0    |  (i-1,j)  |    0
    i  | (i,j-1) |  ( i ,j)  | (i,j+1)
i + 1  |    0    |  (i+1,j)  |    0
'''

# 변화량 컨트롤 익숙해지기!!!!!! 나는 상하좌우 순으로 하고 싶음....

di = [0, 1, 0, -1]  # i의 변화값(우측부터 시계방향)
dj = [1, 0, -1, 0]  # j의 변화값(우측부터 시계방향)
N = 2
M = 3

for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)

# list-2 12p 델타 배열 해석해보기
print('ni nj | i j')
for i in range(N):
    for j in range(N):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj                     # packing, unpacking 사용.
            if 0 <= ni < N and 0 <= nj < M:
                print(f'{ni}  {nj}  | {i} {j}')


# 델타 응용
# ex. NxN 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최댓값(예시는 2칸)

k = 2  # 예시는 2칸
max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]  # i, j를 중심으로
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향
            for c in range(1, k+1):                 # 거리별
                ni, nj = i + di * c, j + dj * c
                if 0 <= ni < N and 0 <= nj < M:
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s