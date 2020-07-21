"""
求矩阵像素的最大连通域，像素为1的pixel周围8*8的像素为1的pixel都是它的邻接点，连接性具有传递性，pixel a与
pixel b连通，b与c连通，则a与c连通，所以找到邻接点后再找邻接点的邻接点。
试找出一个二值矩阵的所有连通域（8邻接），并给出每个连通域的面积（邻接点的个数）和重心。

每组输入包括 M+1 行，第一行输入2个整数 M (1<M<100), N (1<N<100)，其中M是矩阵的行数，N是矩阵的列数。
第2至M+1行，每行 N 个整数，表示在矩阵N列的像素值（已二值化为 0 和 1， 连通域为 1 表示的区域）。

输出 K+1 行，第一行输出连通域个数K，第2至 K+1 行，每行输出3个数，依次表示为连通域的面积值和重心的坐标值（保留2位小数点），
按照连通域起始点顺序输出。
e.g. Input:
4 4
0 1 0 0
0 0 0 1
0 0 0 1
1 0 0 0
Output:
3
1 1.00 0.00
2 3.00 1.50
1 0.00 3.00
"""

"""
# wrong understanding
import operator
def fun():
    result=[]
    dirs=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]
    for i in range(1,row-1):
        for j in range(1,col-1):
            cor=[]
            for dx,dy in dirs:
                if (num_list[i+dx][j+dy] == 1):
                    cor.append((i+dx,j+dy))
            # area=sum(list(num_list[i-1,j],num_list[i+1,j],
            #               num_list[i, j - 1],num_list[i, j+1],
            #               num_list[i - 1, j - 1],num_list[i - 1, j+1],
            #               num_list[i + 1, j - 1],num_list[i + 1, j+1]))
            # print("cor",cor)
            if len(cor)==1 or all(is_connect(cor,t1) for t1 in cor):
                x_sum=0
                y_sum=0
                for t in cor:
                    x,y=t
                    x_sum+=x
                    y_sum+=y
                # mid_x = round(x_sum /len(cor),2)
                # mid_y = round(y_sum / len(cor),2)
                mid_x = '%.2f'% (x_sum / len(cor))
                mid_y = '%.2f'% (y_sum / len(cor))
                result.append((len(cor),mid_y,mid_x))

    print(len(result))
    for ele in result:
        # area,mid_x,mid_y=ele
        print(ele[0],ele[1],ele[2])

def is_connect(cor,t1):
    x1,y1=t1
    for t in cor:
        if(not operator.eq(t,t1)):
            x,y=t
            if(x1==x or y1==y):
                return True
                break
    return False
"""

def fun2():
    count=0
    result=[]
    for i in range(row):
        for j in range(col):
            if(num_list[i][j]):
                x_sum,y_sum,num=dfs(i,j,used,0,0,0)
                count+=1
                result.append((num,y_sum/num,x_sum/num))
    print(count)
    for res in result:
        # print("%d %.2f %.2f" % (res[0],res[1],res[2]))
        print("{} {:.2f} {:.2f}".format(res[0],res[1],res[2]))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

def dfs(i, j, used,x_sum, y_sum, num):
    num_list[i][j]=0  ###### if belongs to other's adjacency, don't need to count its adjacency
    x_sum, y_sum= x_sum + i, y_sum + j
    num+=1
    for ix,iy in dirs:
        if(0<=i+ix<row and 0<=j+iy<col and num_list[i+ix][j+iy] and not used[i+ix][j+iy]):
            used[i+ix][j+iy]=1
            x_sum, y_sum, num=dfs(i + ix, j + iy, used,x_sum, y_sum, num)  #### or add (i+ix,y+iy) to a list
    return x_sum, y_sum, num


if __name__ == "__main__":
    row,col= map(int,input().strip().split())
    num_list=[]
    for i in range(row):
        num_list.append(list(map(int,input().strip().split())))
    # print(num_list)
    used = [[0 for j in range(col)] for i in range(row)]
    fun2()