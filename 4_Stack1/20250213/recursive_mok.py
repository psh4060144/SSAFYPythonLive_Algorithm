# 재귀를 쓰는 case
# 1. 반복문 처럼
# 2. 큰 문제를 해결하기 위해 작은 문제를 해결하는 형태.


N = 5
arr = [0] * N


def my_func(idx, num):
    if idx == N:
        return
    arr[idx] = num
    my_func(idx + 1, num + 10)


my_func(0, 10)
print(arr)


def my_func2(idx):
    if idx == N:
        print(arr)
        return
    arr[idx] = 0
    my_func2(idx + 1)
    arr[idx] = 1
    my_func2(idx + 1)


my_func2(0)


########


def fibo(n):  # fibonacci 수열에서 n 번째 항을 반환하는 함수.
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n - 2)


print(fibo(11))