# string

# 컴퓨터에 문자는 bit 표현으로 모두 저장된다.
# 영어의 경우 대소문자를 모두 합쳐 52자이므로 6bit(000000~111111의 64가지)면 모두 표현할 수 있다.

# 알파벳 이외에 비출력용 제어 문자와 출력용 문자를 포함해 7bit로 인코딩한 것을 ASCII 라고 한다.
# 여기에 더해 8bit로 늘려 특수 문자, 도형, 기호 등의 부가적인 문자를 더한 것을 확장 ASCII 라고 한다.

# 영어 뿐만 아니라 전 세계의 서로 다른 언어를 표현하기 위해 Unicode 라는 새 표준을 만들었다.
# ASCII 코드는 10진수로 표현하고, Unicode 는 16진수로 표현한다.

print(f'{ord("대"):x}')
print(chr(0xb301))

# Unicode 또한 Character Set 으로 분류된다. byte 순서에 대해 표준화하지 못했기 때문.

# big-endian / little-endian
# 컴퓨터가 메모리에 데이터를 읽고 쓰는 방식을 정할 때 생기는 문제를 해결하기 위한 것.

# 일반적으로 모든 글자는 2byte 를 소모한다. 따라서 8bit 로 이루어진 1byte 두 개를 사용한다.
# big-endian: 메모리를 저장할 때 상위 byte, 즉 큰 쪽을 먼저 저장하는 것.
# little-endian: 메모리를 저장할 때 하위 byte, 즉 작은 쪽을 먼저 저장하는 것.
# 일반적인 네트워크에서는 big-endian 으로 통일하고 있음.

# CRLF
# 개행 문자(enter)를 처리하는 방식이 두 가지로 나뉠 때가 있었음.
# CR: \r   /   LF: \n
# windows 에서는 CR과 LF를 둘 다 사용해야 인식한다.
# 따라서 주의할 것.

# UTF-8: 주로 web 에서 사용. 가변 크기. 1byte 기준 8bit ~ 32bit. 처리에 시간이 좀 걸림.
# UTF-16: windows, java. 가변 크기. 2byte 기준 16bit ~ 32bit.
# UTF-32: unix. 4byte 기준 32bit. 처리가 빠르다.

# list(input())과 input()의 차이

s1 = list(input())  # 들어오는 문자열의 모든 문자를 쪼개 list 에 저장한다.
print(s1)  # abc 를 넣으면?

s2 = input()  # 들어오는 문자열을 그대로 문자열로 받는다.
print(s2)  # abc 를 넣으면?

print(s1[1])  # list 는 indexing 이 가능하기 때문.
print(s2[1])  # str 은 indexing 이 가능하기 때문.

# list 내의 요소는 수정 가능하지만 str 내의 글자 하나는 수정이 불가능하다.
# 왜? str 은 immutable 한 자료형이기 때문. 수정이 불가능하다.
# 그럼 str 을 고치려면 어떻게 해야 할까? 쪼개서 고치고 붙이던가, 아니면 통째로 고치던가.

# 문자열의 +, *
s3 = 'ab' * 6
s4 = 'ab' + 'cd'
print(s3)
print(s4)
print(''.join(s2))  # s2 = ['a', 'b', 'c']

# java 에서는, 문자 하나의 type 이 따로 있고(char), 홑따옴표로 표시한다.
# 따라서, java 에서 'abc' 라는 표현을 사용한다면 오류가 난다. "abc" 로 해야 한다.


# 문자열 비교

# java 와 python 의 차이
# java 의 equals()와 python 의 == 는 같은 역할을 한다.
# java 의 == 와 python 의 is 는 같은 역할을 한다.
# 즉, == 는 java 와 python 에서 서로 다르게 동작한다!

e1 = 'abc'
e2 = 'ab'
e4 = e2 + 'c'
print(e1 == e4)
print(e1 is e4)
print(e1 is 'abc')  # SyntaxWarning: "is" with a literal. Did you mean "=="?
print(e4 is 'abc')  # SyntaxWarning: "is" with a literal. Did you mean "=="?
# SyntaxWarning: '글자랑 비교하고 있다. == 를 의도한 거니?' = 안 도는 건 아닌데, 그냥 is 를 함부로 쓰지 말라는 거.

