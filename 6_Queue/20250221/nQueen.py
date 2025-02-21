# n-Queen

N = 4
arr = [[0] * N for _ in range(N)]
check = [0] * 4  # 퀸이 어느 열에 놓여졌는지 표시하는 배열.
# 퀸을 놓는 것은 2차원 배열이지만 열이 겹치지 않는 것을 보려면 1차원 배열로도 충분하다.
dia1 = [0] * (2 * N - 1)
dia2 = [0] * (2 * N - 1)  # 대각선 판별. 모든 대각선을 세서, 안에 퀸이 있는지 확인하기 위해 대각선을 찾아본다.


# row 행에 퀸을 하나 놓아보기
def nqueen(row):
    if row == N:  # row 가 N 이 되었다 = N - 1 행까지 퀸을 놓
        for j in range(N):
            print(arr[j])
        print('=====')
    for i in range(N):  # 모든 열에 퀸을 놓아보기.
        if not check[i] and not dia1[row + i] and not dia2[row - i + N - 1]:
            arr[row][i] = 'Q'
            check[i] = 1
            dia1[row + i] = 1
            dia2[row - i + N - 1] = 1
            nqueen(row + 1)  # 다음 행에 퀸 놓으러 가기
            arr[row][i] = 0  # 다음 열에 퀸을 놓기 위해 먼저번의 퀸을 치워줌.
            check[i] = 0  # 퀸 체크도 해제.
            dia1[row + i] = 0
            dia2[row - i + N - 1] = 0

nqueen(0)