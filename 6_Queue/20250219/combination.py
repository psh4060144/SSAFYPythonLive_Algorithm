# 조합

arr = [1, 2, 3, 4, 5]
N = len(arr)
M = 3  # 구하고 싶은 조합 길이

check = [0] * N  # 각 요소가 조합에 포함되는지 아닌지 표시하는 배열

# check 의 각 index 에 0 또는 1을 넣음. 몇 개가 포함되는 지 알아야 한다.


def combination(idx, cnt):
    if cnt == M:
        print(check)
        return
    if idx == N:  # 정답을 찾지 못한 상태. 마지막 index 까지 M개의 원소를 선택하지 못한 경우.
        return

        # 완전 탐색은~~~
        # cnt = 0
        # for i in range(N):  # 요소가 몇 개 포함되었는지 확인
        #     if check[i]:
        #         cnt += 1
        # if cnt == M:
        #     print(check)
        # return


    check[idx] = 0
    combination(idx + 1, cnt)  # 하나의 상태를 확정하면 다음 index 를 결정하기 위해 재귀 실행.
    check[idx] = 1
    combination(idx + 1, cnt + 1)
    check[idx] = 0  # 이렇게 해도(원래 상태로 돌려줘도) 오류가 없어짐.

    # check[idx] = 1
    # combination(idx + 1, cnt + 1)
    # check[idx] = 0
    # combination(idx + 1, cnt)  # 아니면 이렇게 순서를 바꿔줘도 오류가 없어짐.


combination(0, 0)