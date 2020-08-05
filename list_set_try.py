if __name__ == "__main__":
    a=[1,2,3,4]
    b=[3,3,5,4]
    print(a+b)
    print(set(a+b))  #{1, 2, 3, 4, 5}
    print(set(a).union(set(b)))   #{1, 2, 3, 4, 5}
    print("a和b中相同的元素个数")
    print(len(a+b)-len(set(a+b)))  # a和b中相同的元素个数, 3个
    print()

    print("a和b中相同的元素个数")
    c=set(a).intersection(set(b))  # a和b中相同的元素个数，2个
    print(c,len(c)) #{3, 4} 2
    print()

    print("在a中不在b中的元素")
    print("a=",set(a))
    print("b=",set(b))
    print(set(a)-set(b),len(set(a)-set(b))) # 在a中不在b中的元素 {1,2} 2
    print()

    print("在a中不在b中的元素")
    print(set(a).difference(set(b))) # 在a中不在b中的元素 [1, 2]
    print()

    print("在a中不在b中的元素")
    print([i for i in a if i not in b]) # 在a中不在b中的元素 [1, 2]
    print()

    print("a和b中不同的元素")
    d = set(a+b)
    c = set(a).intersection(set(b))
    e=d-c   # a和b中不同的元素 {1, 2, 5}
    print(e)
    print()

    print("a和b中不同的元素")
    f = set(a).symmetric_difference(set(b))  # a和b中不同的元素  {1, 2, 5}
    print(f)
    print()

    # 定义一个集合
    set1 = {1, 2, 3, 4, 5}
    # 或者使用 set 函数
    list1 = [6, 7, 7, 8, 8, 9]
    set2 = set(list1)
    set2.add(10)  # 添加新元素
    print("set2",set2)  # set([6,7,8,9,10]) 去掉重复内容,
    set2.update([10,11,12])
    print("set2", set2)
    try:
        set3 = frozenset(list1)  # 固定集合
        set3.add(10)  # 固定集合不能添加元素
        print("set3",set3)
    except:
        print("error")



