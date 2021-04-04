"""
The sorted function practice is for https://www.liaoxuefeng.com/wiki/1016959663602400/1017408670135712
假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排
"""
# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0].lower()


def by_score(t):
    return t[1]

if __name__ == "__main__":
    L1 = sorted(L, key=by_name)
    print(L1)

    L1 = sorted(L, key=lambda t: t[0])
    print(L1)


    L2 = sorted(L, key=by_score,reverse=True)
    print(L2)

    L2= sorted(L,key=lambda t:t[1],reverse=True)
    print(L2)
