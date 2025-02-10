# selection sort
# 오름차순 정렬일 때.
# list 전체를 순회해서 가장 작은 수와 첫 번째 자리의 수를 위치 교환.
# 첫 번째 자리의 수는 건드리지 않고 다시 list를 순회해서 가장 작은 수와 두 번째 자리의 수를 위치 교환.
# 위를 반복.

arr = [6, 5, 1, 2, 4, 8, 2, 7]


def selection_sort(arr):        # 요소를 오름차순 정렬.
    N = len(arr)
    # 0번부터 N-1번까지 들어갈 요소 찾아서 바꿔주기
    # i번째에 들어갈 요소를 찾아서 넣어주기
    for i in range(N):          # i: 숫자를 넣는 순서.
        # i번째로 작은 숫자 찾기 : 값이 필요한 게 아니라 위치가 필요한 것!
        min_idx = i             # 왜 i? 위치를 찾은 요소는 제외하고 탐색하기 위해.
                                # 결국 비교 대상이 필요한 거라 min_idx = N - 1로 해도 된다. 이건 index로 쓰기 위해 설정하는 것.
        for j in range(i + 1, N):   # for j in range(i, N): min_idx = N - 1로 했을 때.
            # 기존 최솟값과 요소를 비교.
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]     # 반복문을 완료하면 최솟값의 위치를 교환해줌.


selection_sort(arr)
print(arr)

# 하지만, selection sort는 효율성이 매우 떨어져 거의 사용하지 않는다. 왜? O(n**2)의 시간 복잡도가 들기 때문.
# quick sort는 O(n * log(n))의 시간이 든다. 훨씬 빠르니까 다들 quick sort를 쓴다.
