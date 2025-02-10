# 전치 행렬
# 정사각 행렬의 경우 좌상단-우하단까지 이어진 하나의 대각선을 기준으로 선대칭한 행렬.
# 파이썬에서는 정사각 행렬이 아니더라도 전치행렬을 구할 수 있지만, 일반적으로 정사각 행렬에서 수행하고, 우리도 정사각 행렬을 배운다.

# i = 행의 좌표, len(arr)
# j = 열의 좌표, len(arr[0])

'''
1 2 3
4 5 6
7 8 9
'''

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(3):
    for j in range(3):  # for j in range(i)인 경우 (전 범위를 설정하지 않고 대각선 아래 부분만 설정하는 경우)
        if i < j:       # if문이 필요 없음.
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

'''
i < j   i > j
0 1 1   0 0 0
0 0 1   1 0 0
0 0 0   1 1 0

for i in range(N)
    for j in range(N)
        if문 작성
'''

'''
i == j
1 0 0
0 1 0
0 0 1

for i in range(N)
    if arr[i][i]~
'''

'''
N-1-i == j
   0 0 1
   0 1 0
   1 0 0

for i in range(N)
    if arr[i][N-1-i]~
'''