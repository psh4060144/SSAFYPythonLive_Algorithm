# 최대 99개의 값을 저장 가능한 최대 heap 을 만들어 보자.


def enq(n):
    global last  # 마지막 정점에 대해
    last += 1
    heap[last] = n  # 마지막 정점에 n 저장.

    c = last  # 부모의 키값과 비교하기 위해
    p = c // 2  # 부모 정점 번호 계산

    while p and heap[p] < heap[c]:  # 부모가 있고, 부모가 자식보다 작지 않을 때까지 반복. 왜? 최대 heap 조건에 위배되기 때문에.
        heap[p], heap[c] = heap[c], heap[p]  # 부모와 자식의 자리를 바꿔 줌.
        c = p  # 현재 부모를 자식으로 생각.
        p = c // 2  # 부모의 부모를 다시 찾음.

def deq():
    global last
    tmp = heap[1]  # root backup
    heap[1] = heap[last]  # 삭제할 노드의 키를 root 에 복사
    last -= 1  # 마지막 노드 삭제
    p = 1  # root 에 옮긴 값을 자식과 비교
    c = p * 2  # 왼쪽 자식.

    while c <= last:  # 자식이 하나라도 있으면 반복.
        if c + 1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식도 있고, 오른쪽 자식이 왼쪽 자식보다 더 크다면
            c += 1  # 비교 대상을 오른쪽 자식으로.

        if heap[p] < heap[c]:  # 최대 heap 조건에 위배되지 않는지 확인하기 위해 부모와 자식의 크기를 비교
            heap[p], heap[c] = heap[c], heap[p]  # 크다면 바꿔 주고
            p = c  # 현재 자식을 새로운 부모로 생각.
            c = p * 2  # 왼쪽 자식 번호를 계산.
        else:
            break  # 다 끝났다면 반복 종료.

    return tmp  # 추출한 최댓값 출력


heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)
while last:
    print(deq())