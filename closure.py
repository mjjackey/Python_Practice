"""
The closure practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017434209254976
利用闭包返回一个计数器函数，每次调用它返回递增整数
"""
def createCounter():
    i=0
    def counter():
        nonlocal i
        i+=1
        return i
    return counter

def createCounter1():
    i = [0]  # any other variant type e.g. dict
    def counter():
        i[0] += 1
        return i[0]
    return counter

def createCounter2():
    def gen():
        i = 0
        while True:
            i+=1
            yield  i
    n=gen()
    def counter():
        return next(n)
    return counter

    # wrong
    # def counter():
    #     i = 0
    #     while True:
    #         i+=1
    #         yield  i
    #     return next(counter())
    # return counter

if __name__ == "__main__":
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    counterA = createCounter1()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter1()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    counterA = createCounter2()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter2()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')