'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

v = int(input())
tree = [[None, None] for _ in range(v + 1)]

edges = list(map(int, input().split()))

for i in range(0, (v-1)*2, 2):
    # tree 의 부모 index 에 자식 번호가 저장됨.
    if tree[edges[i]][0] is None:
        tree[edges[i]][0] = edges[i + 1]
    else:
        tree[edges[i]][1] = edges[i + 1]


def preorder(v):
    if v is None:
        return
    print(f'{v}번 방문!', end=' ')
    preorder(tree[v][0])
    preorder(tree[v][1])

preorder(1)
print()
print('===')


def inorder(v):
    if v is None:
        return
    inorder(tree[v][0])
    print(f'{v}번 방문!', end=' ')
    inorder(tree[v][1])

inorder(1)
print()
print('===')


def postorder(v):
    if v is None:
        return
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(f'{v}번 방문!', end=' ')

postorder(1)
print()
print('===')


# 목쌤은 왼쪽 list, 오른쪽 list 를 한 데 묶어서 2차원 list 로 정리하고 있다.