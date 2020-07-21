"""
8 7 3 6
0 1
1 2
2 3
0 3
4 5
5 6
4 7
"""
class Graph():
    def __init__(self,nodes,sides):
        '''
        nodes 表示点, list
        sides 表示边(两个点组成的边), a list of tuple
        '''
        # self.sequence是字典，key是node，value是与key相连接的点(是list)
        self.sequence = {}
        # self.side是临时变量，主要用于保存与指定点相连接的点
        self.side=[]
        for node in nodes:
            for side_tuple in sides:  ## side_tuple is a tuple
                u,v=side_tuple
                # 指定点与另一个点在同一个边中，则说明这个点与指定点是相连接的点，则需要将这个点放到self.side中
                if node == u:
                    self.side.append(v)
                elif node == v:
                    self.side.append(u)
            self.sequence[node] = self.side
            self.side=[]

    # def count(self):
    #      """
    #      wrong method, which might contains the duplicated node
    #      :return:
    #      """
    #      sides_list=[]
    #      print(self.sequence)
    #      combine_list=[]
    #      temp=[]
    #      for k, v in self.sequence.items():
    #          combine_list=v.copy()  ######
    #          combine_list.append(k)
    #          flag=False
    #          for i in range(len(sides_list)):
    #             # if k in sides_list[i]:
    #             #     flag=True
    #             #     break
    #             if(any(ele in sides_list[i] for ele in combine_list)):
    #                 flag=True
    #                 break
    #          if(flag):
    #              # temp=list(sides_list[i]).extend(combine_list) ###### temp=None
    #              # print("temp",temp)
    #              temp=list(sides_list[i])
    #              temp.extend(combine_list)
    #              print("temp",temp)
    #              sides_list[i]=temp.copy()
    #              print("sides_list[i]",sides_list[i])
    #              sides_list[i]=set(sides_list[i])
    #              print("sides_list[i]_2",sides_list[i])
    #          else:
    #              sides_list.append(combine_list)
    #          # v.append(k)
    #          # sides_list.append(v)
    #          # if(set(v) & set(sides_list[i])!=None):
    #          #      v+sides_list[i]
    #          # i=+1
    #
    #      sides_t_list=[]
    #      split_list=[]
    #      for sides in sides_list:
    #          sides_t= set(sides)
    #          if(len(sides_t)==1):
    #              split_list.append(sides_t)
    #          else:
    #              sides_t_list.append(sides_t)
    #      print(sides_t_list)
    #      print(split_list)
    #      cost=2*b+b*(len(sides_t_list)+len(split_list)-1)+a*len(sides_t_list)
    #      return cost

    def DFS(self, node0):
        # queue本质上是栈，用来存放需要进行遍历的数据
        # order里面存放的是具体的访问路径
        queue, order = [], []
        # 首先将初始遍历的节点放到queue中，表示将要从这个点开始遍历
        queue.append(node0)
        while queue:
            # 从queue中pop出点v，然后从v点开始遍历了，所以可以将这个点pop出，然后将其放入order中
            # 这里才是最有用的地方，pop()表示弹出栈顶，由于下面的for循环不断的访问子节点，并将子节点压入堆栈，
            # 也就保证了每次的栈顶弹出的顺序是下面的节点
            v = queue.pop()  #####LIFO
            order.append(v)
            # 这里开始遍历v的子节点
            for w in self.sequence[v]:  #####
                # w既不属于queue也不属于order，意味着这个点没被访问过，所以将其放到queue中，然后后续进行访问
                if w not in order and w not in queue:
                    queue.append(w)
        return order

if __name__ == "__main__":
    n,m,a,b = map(int,input().strip().split())
    nodes = [i for i in range(n)]
    # print(nodes)
    sides=[]
    for i in range(m):
        t= set(map(int,input().strip().split()))
        sides.append(t)
    # print(sides)

    g=Graph(nodes,sides)
    # cost=g.count()
    # print(cost)
    side_list=[]
    side_list_all=[]
    for node in nodes:
        side_list=g.DFS(node)
        # print(side_list)
        side_list_all.append(tuple(sorted(side_list)))

    # print(side_list_all)
    cnt=1
    dict_con={}
    for i in range(len(side_list_all)-1):
        if(side_list_all[i] not in dict_con):
            dict_con.update({side_list_all[i]:1})
        else:
            dict_con[side_list_all[i]]+=1
    cnt=len(dict_con.keys())
    print(len(side_list_all),cnt)
    cost = 2 * b + b * (cnt-1) + a * cnt
    print(cost)








