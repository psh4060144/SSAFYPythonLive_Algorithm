import sys
sys.stdin = open('GNS_test_input.txt', 'r')

num_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())


def bubble_sort(arr):
    for i in range(N - 1):                                  # 요소의 갯수만큼 반복
        for j in range(N - 1):                              # 큰 수를 뒤로 보내는 반복문
            if num_dict[arr[j]] > num_dict[arr[j + 1]]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(arr):
    # i 번째 요소에 i 번째로 작은 요소 가져와서 넣어주기.
    for i in range(N - 1):
        # i 번부터 N - 1 번까지 중에 제일 작은 거 골라서 i 번 위치와 바꿔주기
        min_idx = i

        for j in range(i, N):
            if num_dict[arr[min_idx]] > num_dict[arr[j]]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


    # counting sort 의 제약 조건
    # value 를 index 로 사용이 가능해야 한다.
    # 최솟값과 최댓값의 편차가 적어야 효율적이다.
def counting_sort(arr):
    # 갯수 세기
    count = [0] * 10
    for i in range(N):
        idx = num_dict[arr[i]]
        count[idx] += 1

    # 누적합
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 자리 찾아주기(요소가 들어갈 위치: count 의 각각의 값)
    sorted_arr = [None] * N
    for i in range(N):
        num = num_dict[arr[i]]
        count[num] -= 1
        sorted_arr[count[num]] = arr[i]

    return sorted_arr


    # 정렬된 배열을 반환하는 함수
    # 각 요소의 갯수를 세서, 그 갯수만큼 list 에 붙이기.
def solve(arr):
    num_cnt_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}

    for i in range(N):
        num_cnt_dict[arr[i]] += 1

    sorted_list = []

    for key in num_cnt_dict.keys():
        sorted_list.extend([key] * num_cnt_dict[key])

    return sorted_list


for _ in range(T):

    tc, N = input().split()
    N = int(N)
    data = input().split()

    data = solve(data)

    print(f'{tc}')
    print(*data)

