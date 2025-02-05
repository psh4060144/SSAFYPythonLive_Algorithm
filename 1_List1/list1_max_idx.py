N = int(input())
arr = list(map(int, input().split()))


def finding_first_max_idx(N, arr):

    max_idx = 0

    for i in range(1, N):
        if arr[max_idx] < arr[i]:
            max_idx = i

    return max_idx


def finding_last_max_idx(N, arr):

    max_idx = 0

    for i in range(1, N):
        if arr[max_idx] <= arr[i]:
            max_idx = i

    return max_idx


result1 = finding_first_max_idx(N, arr)
result2 = finding_last_max_idx(N, arr)

print(result1)
print(result2)