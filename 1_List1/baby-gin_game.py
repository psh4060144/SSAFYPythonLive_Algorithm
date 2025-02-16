# Baby-gin Game을 풀어낼 수 있는 두 가지 방법



# 완전 검색(완전 탐색, Exaustive Search, Brute-force, generate-and-test)
# 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 방법.
# 모든 경우의 수를 테스트한 후 최종 해법을 도출하기 때문에, 일반적으로 경우의 수가 상대적으로 작을 때 유용.
# 부분집합, 조합, 순열, DFS, BFS 등.

# 순열: 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열하는 것.
# 서로 다른 n개 중 r개를 택하는 순열 = nPr = n * (n-1) * (n-2) * (n-3) * ... * (n-r+1)
# nPn = n * (n-1) * (n-2) * (n-3) * ... * 2 * 1 = n!(Factorial)

# 중복 순열
arr = [2, 3, 7]
N = len(arr)
result = [0] * 3
new_arr = []
for i1 in range(N):
    for i2 in range(N):
        for i3 in range(N):
            result[i1] = arr[i1]
            result[i2] = arr[i2]
            result[i3] = arr[i3]
            print([arr[i1], arr[i2], arr[i3]])

# arr 내의 모든 인수를 포함하는 순열을 생성하는 함수
arr = [2, 3, 7]
for i1 in range(len(arr)):
    for i2 in range(len(arr)):
        if i2 != i1:
            for i3 in range(len(arr)):
                if i3 != i1 and i3 != i2:
                    print(arr[i1], arr[i2], arr[i3])
# 하지만, 이렇게 적은 갯수의 순열을 만들거라면 그냥 hard coding으로 만들어두고 써도 되긴 한다....
# 이해는 해도, 효율적인 면에서 아쉽다는 걸 반드시 알아둘 것.



# 탐욕 알고리즘(Greedy Algorithm)
# 최적해를 구하는 데 사용되는 근시안적인 방법.
# 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달.
# 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었을 때 그것이 최적이라는 보장은 없음.
# 즉, 내 눈 앞의 미래를 최적으로 결정하더라도 그것이 반드시 옳은 방향으로 나가는 것은 아니라는 것.
# 일반적으로 머릿속에 떠오르는 생각을 검증 없이 바로 구현하면 Greedy 접근이 됨.
# 따라서, Greedy는 매우 조심스럽게 접근해야 하는 알고리즘.

# 동작 과정
# 1. 해 선택: 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합에 추가.
# 2. 실행 가능성 검사: 새로운 부분해 집합이 실행 가능한지를 확인. 즉, 문제의 제약 조건을 위반하지 않는지 검사.
# 3. 해 검사: 새로운 부분해 집합이 문제의 해가 되는지 확인. 아직 전체 문제의 해가 완성되지 않았다면 1)의 해 선택부터 다시 시작.



# Baby-gin Game by Greedy Algorithm
num = int(input())  # Baby-gin 확인할 6자리 수를 입력받음.
c = [0] * 12  # 6자리 수로부터 각 자릿수를 추출하여 갯수를 누적할 리스트

for _ in range(6):
    c[num % 10] += 1  # [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0] 처럼 들어오는 숫자가 1씩 늘어난다.
    num //= 10  # 이러면 1의 자리부터 거꾸로 배열에 들어가게 되지만,
                # 우리가 원하는 Baby-gin은 갯수를 찾는 거지 순서가 상관이 없다. 그러니까 이래도 된다.

i = 0
triplet = run = 0

while i < 10:  # index 1부터 10까지 센다.
    if c[i] >= 3:  # triplet 조사 후 데이터를 삭제하는 부분
        c[i] -= 3
        triplet += 1
        continue  # 여기부터 반복을 처음부터 다시 시작.
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:   # run 조사 후 데이터 삭제. 여기서 오류가 나는 것을 막기 위해 c를 12칸으로 만듦.
                                                        # c를 12칸으로 만들지 않으면 if문으로 추가 조건을 만들어야 한다.
                                                        # 이 if문에 조건으로 i < 7을 추가한다거나...
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue  # 여기부터 반복을 처음부터 다시 시작.
    i += 1

if run + triplet == 2:
    print('Baby-Gin!')
else:
    print('Lose...')
# 이게 왜 되느냐? triplet을 run보다 먼저 꺼냈기 때문에 가능한 일.
# run을 triplet보다 먼저 꺼내면 triplet이 2가 되어 문제가 발생하는 경우가 있다.



# pycharm 부등호 합쳐지는 거 풀기
# ctrl + alt + s -> editor -> font -> Enable font ligatures 해제