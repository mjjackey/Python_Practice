if __name__ == "__main__":
    PI = 3.141592653
    print('PI=%10.3f'%PI) # 精度为3, 总长为10, 需要缩进.

    # 用*从后面的元组中读取字段宽度或精度,可以读取出来精度是3位
    # PI=3.142
    # 没有指定宽度，所以不需要缩进
    print("PI=%.*f" % (3, PI))

    print("PI=%*.3f" % (10, PI))  # 精度为3, 总长为10, 需要缩进.

    str_temp='%.2f %s haha $%d'
    str1 = str_temp % (4.88,'hola',2)
    print(str1)

