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
    """
    Even number ought not be prime number, so omit them
    """
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    """
    :param n: known number, x is the element of the sequence
    :return: bool
    """
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()  #### get a generator
    # print(it)  # one element: 2 and a generator object
    while True:
        n = next(it)  #### keep the whole generator: it
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()