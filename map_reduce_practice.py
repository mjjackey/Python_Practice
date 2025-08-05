"""
map reduce practice for https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
"""
from functools import reduce

"""
1.
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""
def normalize(name):
    nor_name=""
    if (ord(name[0]) >= 97 and ord(name[0]) <= 122):  # the ascii code of lowercase
        nor_name= chr(ord(name[0]) - 32)
    else:
        nor_name=name[0]
    for chr_name in name[1:]:
        if(ord(chr_name)>=65 and ord(chr_name)<=90):  # the ascii code of upper case
            nor_name = nor_name + chr(ord(chr_name) + 32)
        else:
            nor_name = nor_name + chr_name
    return nor_name

def normalize2(name):
    return name.capitalize()

def normalize3(name):
    return name[0].upper()+name[1:].lower()


"""
2. 
Python提供的sum()函数可以接受一个list并求和，
请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
def prod(L):
    return reduce(lambda x,y:x*y,L)

"""
3. 
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""
def str2float(s):
    """

    :param s: str, take string as Iterable
    :return:
    """
    point_len=len(s.split('.')[1])
    def char2num(s):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return DIGITS[s]
    return reduce(lambda x,y:x*10+y,map(char2num,s.replace('.','')))/10**point_len

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float2(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0  # flag variable
    def to_float(f, n):
        nonlocal point
        if n == -1:  # decimal point
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

if __name__ == "__main__":
    # 1.
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    L2 = list(map(normalize2, L1))
    print(L2)

    L2 = list(map(normalize3, L1))
    print(L2)

    # 2.
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    # 3.
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')

    print('str2float(\'123.456\') =', str2float2('123.456'))
    if abs(str2float2('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')