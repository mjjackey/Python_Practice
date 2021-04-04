"""
Input:
4  the number of chess pieces
1 2 4 9  horizontal ordinate
1 1 1 1  vertical ordinate
Output: (the minimum times)
four elements
"""
import sys
if __name__ == "__main__":
    # 读取第一行的n
    input_list=[]
    for i in range(3):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        input_list.append(values)
    print(input_list)

