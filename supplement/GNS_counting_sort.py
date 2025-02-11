# counting sort

digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1, T+1):
    temp = input()  #dummy
    arr = list(map(str, input().split()))
 
    # 카운팅
    cnts = [0] * 10
    for item in arr:
        for j in range(10):
            if item == digit[j]:
                cnts[j] += 1
 
    # 출력
    print(f'#{tc}')
    for i in range(10):
        for j in range(cnts[i]):
            print(digit[i], end=' ')
    print()