"""
The decorator practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584#0
Two layer packages
设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""
# -*- coding: utf-8 -*-
import time
import functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1=time.time()
        fn(*args, **kw)
        t2=time.time()
        print('%s executed in %s ms' % (fn.__name__, t2-t1))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

if __name__ == "__main__":
    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')