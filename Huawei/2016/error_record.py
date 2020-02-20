"""
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理:
1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；(文件所在的目录不同，文件名和行号相同也要合并)
2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16个字符和行号相同，也不要合并)
3.输入的文件可能带路径，记录文件名称不能带路径

In:一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。
    文件路径为windows格式
    如：E:\V1R2\product\fpgadrive.c 1325
Out: 将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如: fpgadrive.c 1325 1
    结果根据数目从多到少排序，数目相同的情况下，按照输入第一次出现顺序排序。
    如果超过8条记录，则只输出前8条记录.
    如果文件名的长度超过16个字符，则只输出后16个字符

E:\V1R2\product\fpgadrive.c 1325
fpgadrive.c 1325 1

e:\3\aa1.txt 2
e:\3\aa1.txt 2
e:\1\aa3.txt 3
e:\2\aa2.txt 3
e:\3\aa1.txt 1
e:\1\aa1.txt 3
"""
import collections
import sys

def fun():
    record = collections.OrderedDict()
    # record={}
    while True:
        try:
            ## input_line=input().strip().split()
            input_line=sys.stdin.readline().strip().split()
            file_name=input_line[0].split('\\')[-1]
            key=str(file_name+(' ')+input_line[1])
            # print("key:",key)

            ### The below input appear the condition: continuous wait for the input
            ## key=input().strip().split('\\')[-1]
            # key=sys.stdin.readline().strip().split('\\')[-1]
            # print("key:",key)

            # input_line=input().strip()
            # index =input_line.rfind('\\')
            # key=input_line[index+1:]
            # print("key:",key)

            if(key not in record):
                # record.update({key:1})
                record[key]=1
            else:
                record[key]+=1
        except:
            # print("error")
            break

    record_out = sorted(record.items(), key=lambda x: x[1], reverse=True)
    # print(record_out)
    for k, v in record_out[:min(len(record_out),8)]:
        if (len(k) > 16):
            print(k[-16:], v)
        elif (len(k)<=16 and len(k)>0):
            print(k, v)

if __name__ == "__main__":
    fun()

