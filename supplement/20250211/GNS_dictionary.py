# dictionary

# 리스트에 외계숫자에 해당하는 값을 저장
digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for tc in range(1, T + 1):
    temp = input()  # dummy
    arr = list(map(str, input().split()))
 
    # 카운팅 (배열)
    cnts = {}
    for item in arr:
        if cnts.get(item):  # 기존 키값이 존재
            cnts[item] += 1
        else:  # 키값이 존재하지 않을 때
            cnts[item] = 1
    # print(cnts)
     
    # 출력
    print(f'#{tc}')
    for key in digit:
        for j in range(cnts[key]):
            print(key, end=' ')
    print()