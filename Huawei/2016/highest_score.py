"""
输入包括多组测试数据。
每组输入第一行是两个正整数N和M（0 < N <= 30000,0 < M < 5000）,分别代表学生的数目和操作的数目。
学生ID编号从1编到N。
第二行包含N个整数，代表这N个学生的初始成绩，其中第i个数代表ID为i的学生的成绩
接下来又M行，每一行有一个字符C（只取‘Q’或‘U’），和两个正整数A,B,当C为'Q'的时候, 表示这是一条询问操作，他询问ID从A到B（包括A,B）的学生当中，成绩最高的是多少
当C为‘U’的时候，表示这是一条更新操作，要求把ID为A的学生的成绩更改为B。
Out:
对于每一次询问操作，在一行里面输出最高成绩.
In:
5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
Out:
5
6
5
9
"""
import sys
def fun():
    """
    does not completely pass the newcoder platform
    :return:
    """
    while True:
        try:
            line = input().strip()
            values = list(map(int, line.split()))
            if(len(values)!=2):
                print("Input format wrong")
                return
            stu_n=values[0]
            if(stu_n<=0 or stu_n>3000):
                print("student number wrong")
                return
            opr_m=values[1]
            if(opr_m<=0 or opr_m>=5000):
                print("operation number wrong")

            line2=input().strip()
            score_list = list(map(int, line2.split()))
            if(len(score_list)!=stu_n):
                print("input number wrong")
                return

            for i in range(opr_m):
                # line3 = sys.stdin.readline().strip()
                line3 = input().strip()
                # print(line3)
                type=line3.split()[0]
                # print(type)
                op_list=list(map(int, line3.split()[1:]))
                if(type=='Q'):
                    start=min(op_list)
                    end=max(op_list)
                    max_score=max(score_list[start-1:end])
                    print(max_score)
                elif(type=='U'):
                    score_list[op_list[0]-1] = op_list[1]
        except:
            break

def try_fun():
    for i in range(2):
        line3 = sys.stdin.readline().strip()
        print(line3)

def fun3():
    while True:
        try:
            stu_n, opr_m = map(int, input().strip().split())
            score_list = list(map(int, input().split()))
            for i in range(opr_m):
                input_cmd = input().split()
                op_list = list(map(int, input_cmd[1:]))
                if(input_cmd[0]=="Q"):
                    # start = min(op_list)
                    # end = max(op_list)
                    start,end = sorted(op_list)
                    max_score = max(score_list[start - 1:end])
                    print(max_score)
                elif(input_cmd[0]=="U"):
                    score_list[op_list[0] - 1] = op_list[1]

        except:
            # print("error")
            return

if __name__ == "__main__":
    fun3()
    print("done")
