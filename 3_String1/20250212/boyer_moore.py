t = 'TTTTTATTAATA'
p = 'TTA'

N = len(t)
M = len(p)


def search(p, t):
    for i in range(N - M + 1):  # t에서 p를 비교할 시작 위치 indexing
        for j in range(M):      # p에서 비교할 위치 indexing
            if t[i + j] != p[j]:
                break
        else:                   # break 에 걸리지 않고 for 문이 끝난 경우 실행
            return i
    return -1


print(search(p, t))
