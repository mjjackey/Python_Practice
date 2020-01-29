if __name__ == "__main__":
    a=[1,2,3,4]
    b=[3,3,4,5]
    print(a+b)
    print(set(a+b))
    print(set(a).union(set(b)))
    print("a和b中相同的元素个数")
    print(len(a+b)-len(set(a+b)))  # a和b中相同的元素个数, 3个
    print()

    print("a和b中相同的元素个数")
    c=set(a).intersection(set(b))  # a和b中相同的元素个数，2个
    print(c,len(c))
    print()

    print("在a中不在b中的元素")
    print("a=",set(a))
    print("b=",set(b))
    print(set(a)-set(b),len(set(a)-set(b))) # 在a中不在b中的元素
    print()

    print("在a中不在b中的元素")
    print(set(a).difference(set(b))) # 在a中不在b中的元素
    print()

    print("在a中不在b中的元素")
    print([i for i in a if i not in b]) # 在a中不在b中的元素
    print()

    print("a和b中不同的元素")
    d = set(a+b)
    c = set(a).intersection(set(b))
    e=d-c   # a和b中不同的元素
    print(e)
    print()

    print("a和b中不同的元素")
    f = set(a).symmetric_difference(set(b))  # a和b中不同的元素
    print(f)



