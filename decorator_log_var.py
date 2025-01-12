"""
The decorator practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584#0
Two layer packages
Three layer packages for pass self-defined parameters
"""
import functools
def log(para):
    if(not isinstance(para,str)):
        def wrapper(*args, **kw):
            print('%s():' % (para.__name__))
            return para(*args, **kw)
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (para, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator


@log
def f1():
    print("no parameter")

@log('execute')
def f2():
    print("has parameter")

if __name__ == "__main__":
    f1()
    f2()
    print(f2.__name__)
