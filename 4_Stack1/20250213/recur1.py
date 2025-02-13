def f(i, N):
    if i==N:    # 중단조건
        return
    else:  # 재귀호출
        print(i, end=' ')
        f(i+1, N)

f(0, 100)
# f(0, 1000) RecursionError: maximum recursion depth exceeded in comparison. 재귀 호출의 깊이에는 한계가 있다.