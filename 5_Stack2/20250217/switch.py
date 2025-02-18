N = int(input())

arr = [0] + list(map(int, input().split()))

M = int(input())

for _ in range(M):
    gender, num = map(int, input().split())


    if gender == 1:
        for i in range(num, N, num):
            arr[i] = 1 - arr[i]  # 1은 0으로, 0은 1으로.

    if gender == 2:
        arr[num] = 1 - arr[num]  # 해당 자리는 대칭이 아니어도 바뀐다.
        step = 1
        while (num - step > 0 and num + step < N) and arr[num - step] == arr[num + step]:
            arr[num - step] = 1 - arr[num - step]
            arr[num + step] = 1 - arr[num + step]
            step += 1

for i in range(1, N + 1):
    print(arr[i], end=' ')
    if i % 20 == 0:
        print()