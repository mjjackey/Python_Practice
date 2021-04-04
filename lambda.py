"""
Lambda practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017451447842528
"""
def is_odd(n):
    return n % 2 == 1

if __name__ == "__main__":
    L = list(filter(is_odd, range(1, 20)))
    print(L)

    L= list(filter(lambda n:n%2==1, range(1, 20)))
    print(L)