tree = [None] * 16
tree[1] = 'A'
tree[2] = 'B'
tree[3] = 'C'
tree[4] = 'D'
tree[6] = 'E'
tree[7] = 'F'
tree[12] = 'G'
tree[13] = 'H'

# 트리의 모든 노드를 순회.

# 전위 순회: VLR. 루트 노드에서 작업 처리(방문)하고, 왼쪽 서브트리, 오른쪽 서브트리 순서로 방문
def preorder(v):  # v번 노드에서 작업 처리하기
    # 왼쪽 자식: 현재 노드(v) * 2 번
    # 오른쪽 자식: 현재 노드(v) * 2 + 1번
    if v > 15 or tree[v] is None:  # 노드 갯수를 넘거나 해당 번호 노드가 없다면...
        return

    print(f'{v}번 = {tree[v]}', end=' ')
    preorder(v * 2)  # 왼쪽 자식 작업 처리
    preorder(v * 2 + 1)  # 오른쪽 자식 작업 처리

preorder(1)
print()

# 중위 순회: LVR
def inorder(v):
    if v > 15 or tree[v] is None:  # 노드 갯수를 넘거나 해당 번호 노드가 없다면...
        return

    inorder(v * 2)  # 왼쪽 자식 작업 처리
    print(f'{v}번 = {tree[v]}', end=' ')
    inorder(v * 2 + 1)  # 오른쪽 자식 작업 처리

inorder(1)
print()

# 후위 순회: LRV
def postorder(v):
    if v > 15 or tree[v] is None:  # 노드 갯수를 넘거나 해당 번호 노드가 없다면...
        return

    postorder(v * 2)  # 왼쪽 자식 작업 처리
    postorder(v * 2 + 1)  # 오른쪽 자식 작업 처리
    print(f'{v}번 = {tree[v]}', end=' ')

postorder(1)
print()