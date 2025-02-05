# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하라.

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_el = 0
    min_el = 0
    for num in range(len(arr)):
        if arr[max_el] < arr[num]:
            max_el = num
        if arr[min_el] > arr[num]:
            min_el = num
    print(f'#{i} {arr[max_el] - arr[min_el]}')