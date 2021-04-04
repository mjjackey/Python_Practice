"""
Filter practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017404530360000
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
"""
def is_palindrome(n):
    return all(str(n)[i]==str(n)[len(str(n))-1-i] for i in range(int(len(str(n))/2)))

def is_palindrome2(n):
    return str(n)==str(n)[::-1]

if __name__ == "__main__":
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')

    output2 = filter(is_palindrome2, range(1, 1000))
    print('1~1000:', list(output2))
    if list(filter(is_palindrome2, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')