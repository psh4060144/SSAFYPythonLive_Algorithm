# 순열 Permutation

arr = ['a', 'b', 'c']
N = len(arr)
perm = [None] * N
used = [0] * N  # 사용한 idx 는 1로 표기, 사용하지 않은 idx 는 0으로 표기.


# idx 번째에 모든 요소 넣어보기
def permutation(idx):

    if idx == N:
        print(perm)
        return

    for i in range(N):
        # if used[i]:
        #     continue
        if not used[i]:  # 여기부터가 backtracking. backtracking = 가지치기.
            perm[idx] = arr[i]
            used[i] = 1
            permutation(idx + 1)
            used[i] = 0


permutation(0)