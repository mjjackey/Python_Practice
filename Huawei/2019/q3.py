"""
First three lines input:
1. the length of array
2. the array
3. the operation number
the format of command is "string a b k"
string U represents update the array from index a to index b(include b),the value is the k power of
each element, then % G=1234567891
string C represents sum all the element from index a to index b(include b)
Note: the purpose of the question is to reduce the time complexity
e.g.:
10
1 2 3 4 5 6 7 8 9 10
7
U 1 3 2
C 2 4
U 5 8 2
C 3 9
U 3 8 3
U 1 9 4
C 1 9
"""
import math
import time
G=1234567891

def fun():
    try:  #  array_range=int(input().strip()) ValueError: invalid literal for int() with base 10: ''
        while True:
            array_range=int(input().strip())
            input_list=list(map(int,input().strip().split()))
            # print(input_list)
            opr_num=int(input().strip())
            # print(opr_num)
            for i in range(opr_num):
                cmd_line=input().strip().split()
                cmd=cmd_line[0]
                cmd_list=list(map(int,cmd_line[1:]))
                # print("inter_list",cmd_list)
                if(cmd=='U'):
                    inter_list = sorted(cmd_list[:-1])
                    # print("inter_list", inter_list)
                    for j in range(inter_list[0],inter_list[1]+1):
                        input_list[j]= int(math.pow(input_list[j],cmd_list[2])) % 1234567891
                        # print(input_list[j])
                elif(cmd=='C'):
                    print(sum(input_list[cmd_list[0]:cmd_list[1]+1]))
    except:
        return

def fun2():
    """
    Use the dictionary for input instead of the list to improve the performance of updating values
     by lookup
    :return:
    """
    try:
        while True:
            array_range=int(input().strip())
            input_list=list(map(int,input().strip().split()))
            print(input_list)
            input_dict={}
            for i in range(array_range):
                input_dict[i]=input_list[i]
            # print(input_dict)
            opr_num=int(input().strip())
            # print(opr_num)
            for i in range(opr_num):
                cmd_line=input().strip().split()
                cmd=cmd_line[0]
                cmd_list=list(map(int,cmd_line[1:]))
                # print("inter_list",cmd_list)
                if(cmd=='U'):
                    inter_list = sorted(cmd_list[:-1])
                    # print("inter_list", inter_list)
                    for j in range(inter_list[0],inter_list[1]+1):
                        input_dict[j]= int(math.pow(input_dict[j],cmd_list[2])) % G
                        # print(input_dict[j])
                elif(cmd=='C'):
                    print(sum(list(input_dict.values())[cmd_list[0]:cmd_list[1]+1]))
    except:
        return

if __name__ == "__main__":
    # start_time=time.time()
    # fun()
    # end_time = time.time()
    # print(end_time - start_time)

    start_time = time.time()
    fun2()
    end_time = time.time()
    print(end_time-start_time)