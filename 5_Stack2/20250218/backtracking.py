# 백트래킹 Backtracking
# 해를 찾는 도증에 막히면 되돌아가서 다시 해를 찾는 방법. 깊이 우선 탐색과 매우 유사하지만, 정답이 아닌 쪽으로는 따라가지 않음.
# 따라서 경우의 수를 많이 줄일 수 있다.
# N-Queen Problem

# 결국 백트래킹이란, 가능성 없는 경우의 수는 수행하지 않는 완전탐색이다. 즉, 가지치기를 한 완전탐색이다.
# 부분집합 중에 합이 10인 부분집합을 출력해라.... 같은 문제.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
M = 10
N = len(arr)
check = [0] * N  # 요소가 1이면 idx 번째 요소는 부분집합에 포함되는 것이라고 설정.

# idx: 요소의 idx. | powerset 함수: 해당 요소가 부분집합에 포함되는지 안 되는지 결정하는 함수
def powerset(idx, tmp_sum):

    if tmp_sum > M:  # 76, 77 line 이 backtracking.
        return

    if idx == N:
        if tmp_sum == M:
            for i in range(N):
                if check[i]:
                    print(arr[i], end = ', ')
            print()
        return

    # 특정 상황에서 모든 경우의 수 수행해보기.
    check[idx] = 1
    powerset(idx + 1, tmp_sum + arr[idx])
    check[idx] = 0
    powerset(idx + 1, tmp_sum)
    pass

powerset(0, 0)