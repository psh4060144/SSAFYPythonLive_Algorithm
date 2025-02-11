# 문자열 뒤집기

# 1
s1 = 'Reverse this strings'
r_s1 = s1[::-1]
print(r_s1)

# 2
s2 = 'Reverse this strings'
r_s2 = list(s2)
r_s2.reverse()
r_s2 = ''.join(r_s2)
print(r_s2)

# 3
s3 = 'Reverse this strings'
r_s3 = list(s3)
for i in range(len(r_s3) // 2):
    r_s3[i], r_s3[len(r_s3) - 1 - i] = r_s3[len(r_s3) - 1 - i], r_s3[i]
r_s3 = ''.join(r_s3)
print(r_s3)

# 4
a = 12345
str_a = list(str(a))
for i in range(len(str_a) // 2):
    str_a[i], str_a[len(str_a) - 1 - i] = str_a[len(str_a) - 1 - i], str_a[i]
str_a = ''.join(str_a)
print(str_a)

# 문자열 비교
# 문자열이 같으면 0 리턴
# e1이 e2보다 사전 순서 상 앞서면 -1 리턴
# e1이 e2보다 사전 순서 상 나중이면 1 리턴


def my_string_compare(e1, e2):
    if e1 < e2:
        return '앞의 것이 뒤의 것보다 앞선다'
    elif e1 > e2:
        return '뒤의 것이 앞의 것보다 앞선다'
    else:
        return '같은 값'


k1 = ' '
k2 = 'abc'
k3 = '123'
k4 = '@'

print(my_string_compare('apple', 'apple'))
print(my_string_compare('Apple', 'apple'))  # 대, 소문자는 대문자가 앞선다.
print(my_string_compare(k1, k2))  # 빈 칸이 문자보다 더 앞에 있다.
print(my_string_compare(k2, k3))  # 숫자가 문자보다 더 앞에 있다. 숫자 - 대문자 - 소문자 순.
print(my_string_compare(k2, k4))  # 특수 문자는 문자보다 앞에 있다.


# 문자열 숫자를 정수로 변환하기 (feat. int 의 우수성)

a = 'A'
b = int(a, 16)  # a를 16진수로 변환한다!!!!!
c = '1001'
d = int(c, 2)  # c를 2진수로 변환한다!!!!!!!!!

print(b)
print(d)


# int()와 같은 atoi() 함수 만들기
# ord(char): 문자열의 ASCII 코드에 대응하는 숫자 반환
# chr(int): 숫자의 ASCII 코드에 대응하는 문자 반환

# 숫자 형태의 문자열을 인수로 받아 숫자를 반환. int()의 역할과 동일한 함수를 짜 보자.
def atoi(character):
    result = 0

    for i in range(len(character)):
        num = ord(character[i] - ord('0'))
        result = result * 10 + num

    return result


def itoa(integer):

    result = ''

    while integer > 0:
        remainder = integer % 10
        integer = integer // 10

        # ord('0') = 48. 따라서 1 + ord('0') = 49. 따라서 chr(49) = '1'
        result = chr(remainder + ord('0')) + result

    return result


print(atoi('321'))
print(itoa(54231))
