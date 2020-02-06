"""
埃氏筛法求素数, from https://github.com/michaelliao/learn-python3/blob/master/samples/functional/prime_numbers.py
"""
def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    # print(it)  # one element: 2 and a generator object
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()