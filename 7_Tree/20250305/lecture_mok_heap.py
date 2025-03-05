# 힙 heap
# stack, queue 와 비슷한 개념. 자료구조의 일종.
# 1. 부모 노드가 자식 노드보다 항상 크다 or 항상 작다. | 2. 완전 이진 트리를 유지한다. 가 heap 의 조건.
# stack 은 넣은 역순으로 나오고, queue 는 넣은 정순으로 나오는데 heap 은 넣은 값이 정렬되어 나온다.
# 그러니까, 어떻게 넣든 제일 큰 값부터 차례대로 나오거나 제일 작은 값부터 차례대로 나온다.
# 그 값은 어디서 뽑느냐? root node 에서 뽑는다.
# 나중에 어디서 쓰느냐? prim 알고리즘이나 다익스트라 알고리즘 이런 게 있는데, 그 때 쓴다.

heap = [0] * 10
heapcount = 0


# 부모가 자식보다 무조건 큰 heap(큰 값부터 정렬하는 heap)을 만들어보자.
def heappush(data):
    # 1. 완전 이진 트리의 마지막에 요소 추가.
    # 2. 부모 요소와 값을 비교하면서 자리를 바꾸는 걸 반복. (root node 가 되거나 부모 노드가 더 클 때까지)
    global heapcount
    heapcount += 1
    heap[heapcount] = data
    current = heapcount
    parent = current // 2

    while True:

        if current == 1 or heap[current] < heap[parent]:
            break

        if heap[current] > heap[parent]:
            heap[current], heap[parent] = heap[parent], heap[current]

        current = parent
        parent = current // 2

heappush(2)
print(heap)
heappush(5)
print(heap)
heappush(7)
print(heap)
heappush(4)
print(heap)
heappush(10)
print(heap)
heappush(11)
print(heap)


def heappop():
    # 1. root node 반환 및 삭제
    # 2. 마지막 요소를 root node 로.
    # 3. 자식들 중 큰 값과 비교해서 그 값보다 작으면 바꾸기.
    # 4. 자식들보다 값이 크거나 leaf node 라면 중지.
    global heapcount
    result = heap[1]  # 기존 root node 저장. return 하기 위해.
    heap[1] = heap[heapcount]  # 마지막 요소를 root node 에 저장
    heapcount -= 1

    current = 1
    child = current * 2

    while True:
        if child > heapcount:  # 자식이 없으면
            break

        if child + 1 <= heapcount:  # 오른쪽 자식이 있다면. 왜 이게 오른쪽 자식이 있다면 인가?
            # 그거야, heapcount 가 가장 마지막 node 번호이기 때문.
            if heap[child + 1] > heap[child]:
                child += 1

        if heap[current] < heap[child]:
            heap[current], heap[child] = heap[child], heap[current]

        current = child
        child = current * 2

    return result

print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
print(heap)
print(heappop())
