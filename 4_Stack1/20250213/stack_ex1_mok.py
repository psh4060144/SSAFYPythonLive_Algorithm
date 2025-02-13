# stack 을 만들기 위해 필요한 것
# 1. list: 데이터를 저장하는 목적
# 2. top 변수: stack 의 마지막 요소를 가리키는 변수
# 3. push, pop 이라는 행동을 수행
# => 객체와 완벽하게 동일한 특성.

# => stack 은 class 로 만들면 된다!


class MyStack:

    def __init__(self, len):
        self.max_size = len
        self.s = [None] * len
        self.top = -1

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def isfull(self):
        if self.top + 1 == self.max_size:
            return True
        return False

    def push(self, data):
        if not self.isfull:
            self.top += 1
            self.s[self.top] = data
        else:
            # raise IndexError
            print('가득 참!')

    def pop(self):
        if not self.isempty():
            value = self.s[self.top]
            self.top -= 1
            return value
        return None


stack = MyStack(5)
stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')
stack.push('E')
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())


# 굳이 class 를 만들지 않아도 아래처럼 stack 을 사용 가능하지만, class 를 만드는 게 가장 좋다.


stack2 = [None] * 10000  # 내가 필요로 하는 길이만큼 만들어주기
top = -1

top += 1
stack2[top] = 'a'
top += 1
stack2[top] = 'b'
top += 1
stack2[top] = 'c'
top += 1
stack2[top] = 'd'

print(stack2[top])
top -= 1
print(stack2[top])
top -= 1
print(stack2[top])
top -= 1
print(stack2[top])
top -= 1

