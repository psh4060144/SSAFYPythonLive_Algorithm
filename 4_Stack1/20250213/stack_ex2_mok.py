def my_func1():
    a = 10
    print(f'my_func1 > a : {a}')
    my_func2()


def my_func2():
    a = 5
    my_func3()
    print(f'my_func2 > a : {a}')


def my_func3():
    a = 3
    print(f'my_func3 > a : {a}')


my_func1()
