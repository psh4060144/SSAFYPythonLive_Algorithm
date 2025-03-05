# 이진 트리 연습

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''


def pre_order(T):  # 전위 순회
    if T:  # 0이 아니라면(존재하는 정점이라면)
        print(T, end=' ')  # visit(T). T 에서 할 일 처리.
        pre_order(left[T])  # 왼쪽 자식(서브 트리)로 이동
        pre_order(right[T])  # 오른쪽 자식(서브 트리)로 이동


def in_order(T):  # 중위 순회
    if T:  # 0이 아니라면(존재하는 정점이라면)
        in_order(left[T])  # 왼쪽 자식(서브 트리)로 이동
        print(T, end=' ')  # visit(T). T 에서 할 일 처리.
        in_order(right[T])  # 오른쪽 자식(서브 트리)로 이동


def post_order(T):  # 후위 순회
    if T:  # 0이 아니라면(존재하는 정점이라면)
        post_order(left[T])  # 왼쪽 자식(서브 트리)로 이동
        post_order(right[T])  # 오른쪽 자식(서브 트리)로 이동
        print(T, end=' ')  # visit(T). T 에서 할 일 처리.


N = int(input())  # 1번부터 N번까지의 정점
E = N - 1  # 간선 수. 왜? 이진 트리이니까 간선은 무조건 정점 갯수보다 하나 적다.
arr = list(map(int, input().split()))

left = [0] * (N + 1)  # 부모를 index 로 왼쪽 자식 저장
right = [0] * (N + 1)  # 부모를 index 로 오른쪽 자식 저장
par = [0] * (N + 1)  # 자식을 index 로 부모를 저장

for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]  # parent, child
    par[c] = p

    if left[p] == 0:  # 왼쪽 자식이 아직 없다면
        left[p] = c  # 왼쪽 자식으로써 삽입
    else:
        right[p] = c  # 있다면 오른쪽 자식으로써 삽입

print(left)
print(right)

root = 1
for i in range(1, N + 1):  # root node 를 찾는 for 문.
    if par[i] == 0:  # 부모 정점이 없다면 root node.
        root = i
        break

pre_order(root)  # 1번부터 전위 순회
# print()
# in_order(1)  # 1번부터 중위 순회
# print()
# post_order(1)  # 1번부터 후위 순회


# 영준이형은 왼쪽 list, 오른쪽 list 를 나눠서 각각 저장하고 있다.