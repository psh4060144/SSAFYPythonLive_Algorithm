# 이진 검색(Binary Search)

# 원리
# 0. 탐색 대상은 """반드시""" 정렬된 상태여야 한다.
# 1. 탐색 대상의 중간 위치의 값과 key를 비교. 탐색 범위는 ((첫 번째 index(start) + 마지막 index(end)) // 2).
# 2. 중간의 값과 key가 같다면 탐색 성공, 다르다면 중간값과 key의 크기 비교를 수행.
# 3-1. key가 중간의 값보다 크다면 더 큰 쪽의 절반((중간값 index + 1) ~ end)을 다시 탐색 영역으로 정함.
# 3-2. key가 중간의 값보다 작다면 작은 쪽의 절반(start ~ (중간값 index - 1))을 다시 탐색 영역으로 정함.
# 4. 1~3을 반복하여 탐색.

# 알고리즘 자체는 반드시 숙지해야 함. 이진 검색이 뭐냐? 했을 때 '절반씩 잘라서 중간값을 찾는 과정을 반복해서 찾는 방법이다'라는 생각이 바로 떠올라야 함.
# 익숙하게 만드는 게 제일 크다.

arr = [1, 2, 3, 4, 5, 6, 7, 9, 11, 13, 14, 15, 16, 17, 20, 25, 30]


def binary_search(arr, start, end, key):    # arr: 탐색 대상 / start: 탐색 시작 index / end: 탐색 종료 index / key: 찾는 값

    while start <= end:             # start, end의 범위를 재지정하면서 반복. 범위를 True로 잡고 아래 주석 조건을 달아도 되고,
                                    # 지금처럼 범위 자체를 만들어줘도 된다.

        # if end < start:           # 값이 없다면 while문을 반복하다 end와 start의 index값이 역전된다.
        #     break                 # 이 경우, 탐색 실패.

        mid = (start + end) // 2    # 중간값 설정

        if arr[mid] == key:
            return True             # key가 대상 안에 있음. 따라서, True 반환.

        elif arr[mid] > key:        # 중간값이 key와 다르므로 크기를 비교.
            end = mid - 1           # 더 크다면 중간값보다 작은 영역을 새로 탐색 영역으로 지정해줘야 함.

        else:                       # 크기를 비교.
            start = mid + 1         # 더 작다면 중간값보다 큰 영역을 새로 탐색 영역으로 지정해줘야 함.

    return False                    # key값을 찾지 못했을 때에만 while 문이 종료된다. 따라서, False 반환.


print(binary_search(arr, 0, len(arr) - 1, 19))


# Binary Search Recursive. 재귀 이진 탐색!
# 재귀 함수를 짤 때는, 재귀 자체의 목적을 정확하게 호출해야 함.
# 재귀 이진 탐색의 본질적인 목표, 역할: 지정한 영역 내에 key값이 있다면 True, 없다면 False 반환.
# 내가 짜려고 하는 재귀 함수 전체를 볼 필요는 없다. 애초에 봐서는 재귀를 짤 수가 없다.
# 가장 작은 단위를 생각하고, 그걸 확장할 생각으로 만들어야 한다.


def binary_search_recursive(arr, start, end, key):

    if start > end:             # start와 end의 범위가 역전되는 경우 False 반환.
        return False

    mid = (start + end) // 2

    if arr[mid] == key:
        return True

    elif arr[mid] > key:        # 중간 이후 영역은 볼 필요가 없는 부분.
        return binary_search_recursive(arr, start, mid - 1, key)

    else:                       # 중간 이전 영역은 볼 필요가 없는 부분.
        return binary_search_recursive(arr, mid + 1, end, key)


print(binary_search_recursive(arr, 0, len(arr) - 1, 21))
