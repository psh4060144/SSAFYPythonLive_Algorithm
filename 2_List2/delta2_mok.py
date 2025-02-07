arr = [
    [ 1, 2, 3, 4, 5],
    [ 6, 7, 8, 9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
]  # == [[x for x in range(s,s+5)] for s in range(1, 25, 5)]. list comprehension 연습하기.
N = len(arr)

# 상하좌우 4방향에 접근을 할 수 있도록 변화량 배열을 선언. 변화량이 1이라 변화량 배열이지만 배열의 방향을 말하는 것이기도 함.
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]  # 상하좌우 순서대로.
K = 2

# row 행의 col 열.

for row in range(N):
    for col in range(N):
        # print(arr[row][col])  # 행 우선 순회
        # 현재 좌표 = (row, col)
        sum_v = 0

        for d in range(4):  # d = 방향을 나타내는 변수

            for k in range(1, K + 1):  # k칸 만큼의 합을 구하기 위해 서치 범위를 늘려줌. 단, 아래 식에서 곱셈을 수행하기 위해 1부터 시작.

                trgt_row = row + d_row[d * k]  # 범위를 늘리기 위해 기존 부호 설정에 길이를 곱해주는 것.
                trgt_col = col + d_col[d * k]
                if 0 <= trgt_row < N and 0 <= trgt_col < N:  # 정상범위 내의 결과만 출력하기 위한 부분.  # pythonic한 코드.
                                                             # trgt_row >= 0 and trgt_row < N) and (trgt_col >= 0 and trgt_col < N 이 일반적.
                    sum_v += arr[trgt_row][trgt_col]

        print(sum_v)
    #
    # for row in range(N):
    #     for col in range(N):
    #         print(arr[col][row])  # 열 우선 순회. 행 우선 순회와 열 우선 순회를 골라야 할 때는 조건보다 변수의 위치를 바꾼다.