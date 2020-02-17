def fun():
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

def fun1(oraSet,left_server,memo):
    if (oraSet., left_server) in memo:
        result = memo[oraSet[0], left_server)]
    elif oraSet == [] or left_server == 0:
        result = (0, ())
    elif oraSet[1] > left_server:
        result = fun (oraSet[1:], left_server, memo)
    else:
        nextItem = oraSet[0]

        leftValue, leftToken = fun1(oraSet[1:], left_server - nextItem.getWeight(), memo)
        leftValue += nextItem.getValue()

        rightValue, rightToken = fun1(oraSet[1:], left_server, memo)

        if leftValue > rightValue:
            result = (leftValue, leftToken + (nextItem,))
        else:
            result = (rightValue, rightToken)

    memo[(len(oraSet), left_server)] = result

    return result

if __name__ == "__main__":
    # fun()
    task_dict = {'task1': (300, 20),
                 'task2': (500, 30),
                 'task3': (620, 50),
                 'task4': (370, 30),
                 'task5': (400, 50),
                 'task6': (450, 30),
                 'task7': (380, 40),
                 'task8': (150, 10)
                 }
    server_num = int(input().strip())