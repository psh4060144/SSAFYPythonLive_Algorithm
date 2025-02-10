# 2차원 배열의 선언
# 1차원 list를 묶어놓은 list.
# 2차원 이상의 다차원 list는 차원에 따라 index를 선언.
# 2차원 list의 선언: 세로길이(행의 갯수), 가로길이(열의 갯수)를 필요로 함.
# python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능.

# 입력을 2차원 배열에 저장하기

'''
3
1 2 3
4 5 6
7 8 9
'''

N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
3
123
456
789
'''

N = int(input())
arr2 = [list(map(int, input())) for _ in range(N)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

'''
0 0 0 0
0 0 0 0
0 0 0 0
'''

N = int(input())
arr3 = [[0] * 4 for _ in range(N)]  # [[[0] * 4] * 4] 이건 안됨!!! 왜? 이건 얕은 복사니까.
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

'''
N
0 0 0 ... 0
0 0 0 ... 0
0 0 0 ... 0
. . . ... 0
. . . ... 0
. . . ... 0
0 0 0 ... 0
'''

N = int(input())
arr4 = [[0] * N for _ in range(N)]

# 배열 순회: n x m 배열의 n * m 개의 모든 원소를 빠짐없이 조사하는 방법.

# i 행의 좌표
# j 열의 좌표
for i in range(N):  # 바깥쪽이 행
    for j in range(N):  # 안쪽이 열
        print(arr[i][j])

# 2차원 배열의 합
# N x M 배열의 크기와 저장된 값이 주어질 때 합을 구하는 방법

'''
3 4  # 행 갯수: 3 / 열 갯수: 4
1 7 2 8
6 2 9 3
5 7 4 2
'''

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 행 갯수만큼 반복

s = 0
for i in range(N):
    for j in range(M):
        s += arr[i][j]

# 행의 합 중 최댓값
max_v = 0
for i in range(N):

    row_sum = 0

    for j in range(M):
        row_sum += arr[i][j]

    if max_v < row_sum:
        max_v = row_sum

print(max_v)

# 2차원 배열의 접근

# i 행의 좌표
# j 열의 좌표
for j in range(M):  # 바깥쪽이 행
    for i in range(N):  # 안쪽이 열
        print(arr[i][j])

# 지그재그 순회
# i 행의 좌표
# j 열의 좌표
for i in range(N):  # 바깥쪽이 행
    if i % 2 == 0:  # 안쪽이 열
        for j in range(M):
            pass
    else:
        for j in range(M - 1, 0, -1):
            pass

for i in range(N):  # 바깥쪽이 행
    for j in range(M):
        print(arr[i][j + (M - 1 - 2 * j) * (i % 2)]) # M - 1 - j를 쓰고 싶은데, 정순 배열도 써야하니까 j + ()로 들어가는 거고,
                                                     # 그 때의 정순 배열 index를 위해 i % 2를 곱해서 0처리를 해준다...?

