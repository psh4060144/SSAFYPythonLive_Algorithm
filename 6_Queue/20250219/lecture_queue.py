# 큐 Queue
# stack 과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조.
# queue 의 뒤에서는 삽입만 하고, queue 의 앞에서는 삭제만 이루어지는 구조.
# = 선입선출. (FIFO, First In First Out)
# queue 에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소가 가장 먼저 삭제됨.

# queue 생성
lst = [1, 2, 3]

queue = [0] * 3
front = rear = -1


# queue 에 값 집어넣기

# rear += 1
# queue[rear] = 1
#
# rear += 1
# queue[rear] = 2
#
# rear += 1
# queue[rear] = 3
# =>
for i in range(len(lst)):
    rear += 1
    queue[rear] = lst[i]
print(queue)


# queue 에서 값 꺼내기 : 값을 출력하긴 하지만, 실제로 진짜 꺼낸 것은 아니다. 그대로 남아았긴 하다.
# front += 1
# print(queue[front])
#
# front += 1
# print(queue[front])
#
# front += 1
# print(queue[front])
# +>
while front != rear:
    front += 1
    t = queue[front]
    print(t)
print(queue)


# 선형 queue 이용시의 문제점
# 잘못된 포화상태 인식: 원소의 삽입과 삭제를 반복할 경우 배열의 앞부분에 활용할 수 있는 공간이 있음에도 포화상태(rear = n - 1)로 인식하여 삽입을 하지 않는 경우가 존재.
# 해결방법1: 매 연산마다 저장된 원소들을 배열의 앞부분으로 모두 이동. 이러면 이동에 시간이 걸려서 queue 의 효율성이 급락.
# 해결방법2: 원형 queue 사용. 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 queue 를 이룬다고 가정.

# 원형 queue
# 초기 공백 상태: front = rear = 0
# index 순환: front 와 rear 의 위치가 배열의 마지막 index 인 n - 1 을 가리킨 후, 그 다음에는 논리 순환을 통해 첫 index 인 0이 되어야 함. % 이용.
# front 변수: 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front 가 있는 자리는 사용하지 않고 항상 빈자리로 둠.

# 공백 상태 및 포화상태 검사: isEmpty(), isFull()
# 공백 상태: front = rear
# 포화 상태: 삽입할 rear 의 다음 위치 = 현재 front 의 위치. (rear + 1) % n == front
# 삽입: enQueue(item). 마지막 원소 뒤에 새 원소를 삽입하기 위해 1) rear 값을 조정해서 새 원소를 삽입할 자리를 마련 2) 그 index 에 item 을 저장.
# 삭제: deQueue(). 가장 앞의 원소를 삭제하기 위해 1) front 값을 조정해 삭제할 자리를 준비 2) 새 front 원소를 return. 실제로 삭제는 하지 않긴 함.