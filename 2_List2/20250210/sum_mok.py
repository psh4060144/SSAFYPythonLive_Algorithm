# arr을 순회하면서 행, 열, 대각선의 합 중 최댓값을 반환하는 함수
# integer = 4 byte. = 32bit. 즉, int가 표현할 수 있는 최대의 숫자 갯수는 4294964294. 이걸 양수, 음수로 나눠서 표현하기 때문에, 최대한의 숫자는 2147483647. 익숙하지요?

def solve(arr):
    max_sum = -0xffffffff # 32개의 0을 만들어줘서 최대한 작은 값을 만들어줌.
    for row in range(100):
        row_sum = 0

        for col in range(100):          # row 행 하나를 순회하는 반복문
            row_sum += arr[row][col]    # row 행 요소를 하나씩 더해주기

        if row_sum > max_sum:           # 행의 합이 기존 최댓값보다 크면 교체.
            max_sum = row_sum

    for row in range(100):
        col_sum = 0

        for col in range(100):          # col 열 하나를 순회하는 반복문
            col_sum += arr[col][row]    # col 열 요소를 하나씩 더해주기

        if col_sum > max_sum:           # 열의 합이 기존 최댓값보다 크면 교체.
            max_sum = col_sum

    rightup_sum = 0     # 우상향. row + col == N -1
    rightdown_sum = 0   # 우하향. row == col

    for row in range(100):                      # 대각선 합.(행 우선 순회를 하면서 조건에 맞는 애들끼리 더해주기)
        for col in range(100):

            if row == col:                      # 우하향인 인수만 추가.
                rightdown_sum += arr[row][col]

            elif row+ col == 99:                # 우상향인 인수만 추가.
                rightup_sum += arr[row][col]

    max_sum = rightup_sum if rightup_sum > max_sum else max_sum
    max_sum = rightdown_sum if rightdown_sum > max_sum else max_sum     # 삼항 표현식

T = 10

for _ in range(T):
