"""
 在证明数素无穷性时，使用了一个表达式 N＝2＊3＊5＊7＊11…….＊P + 1，其中 P 为一个素数，N 是 2 到 P 中所有素数的乘积加 1，
 若 P 为最大的素数，可以反证出 N 也是素数，从而证明素数是无穷多的。
 但有人因此认为，所有的 N 都是素数。如N0 = 3 为 素数，N1 = 7 为素数，N2 = 31 为素数。请判断第 i 个 N 是否为素数。

In: 每组输入只有一行，包含一个整数i(0 <= i <= 14)，表示要检查的是第i个N。
Out: 输出只有一行，若Ni为素数，打印“Ni is a prime”，否则打印“Ni is not a prime”。

e.g.
In: 1
Out: 7 is a prime
"""
import  math
def _odd_iter():
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
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def fun(i):
    # prime_list=iter(primes())[:i]
    prime_list=[]
    for num in primes():
        prime_list.append(num)
        if(len(prime_list)==i+1): break
    # print(prime_list)
    prod=1
    for num in prime_list:
        prod=prod*num
    n=prod+1
    flag=False
    for j in range(2,int(math.sqrt(n))+1):
        if(n%j==0):
           flag=True
           break
    if(flag): print(str(n)+" is not a prime")
    else: print(str(n)+ " is a prime")

if __name__ == "__main__":
    i= int(input().strip())
    fun(i)