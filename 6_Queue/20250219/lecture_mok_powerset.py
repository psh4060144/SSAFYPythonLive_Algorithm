# powerset

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
M = 45
check = [0] * N

def powerset(idx,tmp_sum):
    if tmp_sum > M:
        return
    if idx == N:
        if tmp_sum == M:
            for i in range(N):
                if check[i]:
                    print(arr[i], end=',')
            print()
        return

    check[idx] = 1
    powerset(idx + 1, tmp_sum + arr[idx])
    check[idx] = 0
    powerset(idx + 1, tmp_sum)

powerset(0, 0)