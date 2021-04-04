"""
The decorator practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584#0
Three layer packages for pass self-defined parameters
"""
import time
import functools

def log(text1, text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text1, func.__name__))
            # func(*args, **kw)
            func()
            print('%s' % text2)
            return func
        return wrapper
    # print('%s' % text2)
    return decorator

@log('begin call','end call')
def now():
    print(time.time())

if __name__ == "__main__":
    now()