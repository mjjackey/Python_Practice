"""

"""
def greedy():
    try:
        while True:
            task_dict={'task1':(300,20),
                       'task2':(500,30),
                       'task3':(620,50),
                       'task4':(370,30),
                       'task5':(400,50),
                       'task6':(450,30),
                       'task7':(380,40),
                       'task8':(150,10)
                       }
            server_num=int(input().strip())
            total_server=0
            result=[]
            task_dict2=sorted(task_dict.items(),key=lambda x:x[1][1])
            # print(task_dict2)
            for k,v in task_dict2:
                if(total_server+v[1]<=server_num):
                    result.append(v[0])
                    total_server+=v[1]
                else:
                    break

            print(sum(result))
    except:
        return

def fun1(file_server_set, left_server, memo={}):
    if (len(file_server_set), left_server) in memo:
        result = memo[file_server_set[0], left_server]
    elif file_server_set == [] or left_server == 0:
        result = (0, ())
    elif file_server_set[1][2] > left_server:
        result = fun1(file_server_set[1:], left_server, memo)
    else:
        nextItem = file_server_set[0]

        leftValue, leftToken = fun1(file_server_set[1:], left_server - nextItem[2], memo)
        leftValue += nextItem[1]

        rightValue, rightToken = fun1(file_server_set[1:], left_server, memo)

        if leftValue > rightValue:
            result = (leftValue, leftToken + (nextItem[0],nextItem[1],nextItem[2]))
        else:
            result = (rightValue, rightToken)

    memo[(len(file_server_set), left_server)] = result

    return result

if __name__ == "__main__":
    # greedy()
    task_list=['task1','task2','task3','task4','task5','task6', 'task7','task8']
    file_list=[300,500,620,370,400,450,380,150]
    server_list=[20,30,50,30,50,30,40,10]
    item_list=[]
    for i in range(len(task_list)):
        item_list.append([task_list[i],file_list[i],server_list[i]])

    try:
        while True:
                server_num = int(input().strip())
                result=fun1(item_list,server_num)
                print(result[0])
    except:
        print('error')
