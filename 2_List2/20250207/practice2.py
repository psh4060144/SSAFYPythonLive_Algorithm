# 연습문제 2
# 5x5 2차 배열에 25개의 숫자를 저장하고, 25개의 각 요소에 대해 그 요소와 이웃한 요소와의 차의 절댓값을 구하시오.
# 25개의 요소에 대해 모두 조사하여 총합을 구하시오.

T = int(input())

for k in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                ni, nj = i+di, j+dj                     # packing, unpacking 사용.
                if 0 <= ni < N and 0 <= nj < N:
                    total += abs(arr[ni][nj] - arr[i][j])  # abs = 절댓값을 구하는 함수
    print(total)