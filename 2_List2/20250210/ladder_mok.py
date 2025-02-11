# txt 파일로부터 입력 읽어오기
# input() >>> (표준입력으로부터) 한 줄 읽어오기
# 표준 입력을 터미널이 아니라 파일 입력으로 변경

import sys
sys.stdin = open('input_ladder1.txt', 'r')
# sys.stdout = open('output_ladder1.txt', 'r')


# 목적지(2)에 도달하는 x의 열 번호를 반환하는 함수
def solve():
    # 상(0), 좌(1), 우(2) 방향으로 움직일 예정.
    direction = 0  # 사다리의 시작은 항상 위. 즉, 현재 이동 방향.

    row_dir = [-1, 0, 0]
    col_dir = [0, -1, 1]

    #  현재 위치
    row = 99
    col = -1

    # 2의 col 찾기
    for i in range(100):

        if ladder[row][i] == 2:
            c = i
            break

    while True:

        if row == 0:
            break

        # 위쪽으로 올라가고 있을 때는, 양 옆을 확인해야 함.
        if direction == 0:  # (row, col): 현재 위치

            if col > 0 and ladder[row][col - 1] == 1:   # 열 번호가 0보다 크고 오른쪽으로 가는 길이 있다면
                direction = 1                           # 오른쪽으로 간다. 즉, 첫 번째 열에서는 좌회전하지 않는다.

            elif col < 99 and ladder[row][col + 1] == 1:  # 열 번호가 99보다 작고 왼쪽으로 가는 길이 있다면
                direction = 2                           # 왼쪽으로 간다. 즉, 마지막 열에서는 우회전하지 않는다.

        else:       # 현재 왼쪽 또는 오른쪽으로 이동하는 경우
                    # 위쪽으로 가는 길이 있는지 확인.
            if ladder[row - 1][col] == 1:   ##### 여기서 오류가 나긴 하는데... 뭐지...?
                d = 0

        # 한 칸 이동
        row += row_dir[direction]
        col += col_dir[direction]

    # while 문이 끝났을 때, 열 위치는 col 값이므로 col 을 반환.
    return col


def solve2():

    row = 99
    col = -1

    for i in range(100):
        if ladder[row][i] == 2:
            col = i
            break

    while True:  # row 의 좌표를 1씩 줄이는 반복문

        if row == 0:
            break

        # 좌표를 줄이기 전에 양 옆에 갈 수 있는 길이 있으면 끝까지 간다.
        if col > 0 and ladder[row][col - 1] == 1:
            while col > 0 and ladder[row][col - 1] == 1:
                col -= 1

        elif col < 99 and ladder[row][col + 1] == 1:
            while col < 99 and ladder[row][col + 1] == 1:
                col += 1

        row -= 1

    return col


T = 10

for _ in range(1, T + 1):

    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    result = solve2()
    print(f'#{tc} {result}')
