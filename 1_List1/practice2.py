# gravity. 교재 31p.

N = int(input())
arr = list(map(int, input().split()))

max_el_idx = 0
box_drop = 0

for i in range(N):

    if arr[max_el_idx] < arr[i]:
        max_el_idx = i

for i in range(max_el_idx, N - max_el_idx):  # 여기 수정해야 할듯.
    if arr[max_el_idx] > arr[i]:
        box_drop += 1

print(box_drop)