import math
def generate_prime():
    n=100
    pri_num_list=[]
    for num in range(2, n + 1): # the range of candidate numbers
        if all(num % j != 0 for j in range(2, int(math.sqrt(num))+1)):
            # Try divide 2 to sqrt(num)
            ##### Actually, for num=2 or num=3, inner loop does not do, the all returns true
            ##### because if the iterable is empty, all still return true,but 2,3 are prime
            pri_num_list.append(num)

    print(len(pri_num_list),pri_num_list)

def generate_prime1():
    n=100
    pri_num_list = [num for num in range(2, n + 1) if all(num % j != 0 for j in range(2, int(math.sqrt(num)+0.5) + 1))]
    print(len(pri_num_list), pri_num_list)

def generate_prime2():
    n = 100
    pri_num_list = []
    for num in range(2,n+1): # the range of candidate numbers
        flag = True
        for j in range(2, int(math.sqrt(num)+0.5)+1):  # Try divide 2 to sqrt(num)
            if(num%j==0):
                flag=False
                break
        if(flag):
            pri_num_list.append(num)
    print(len(pri_num_list), pri_num_list)

def generate_prime3():
    n = 100
    pri_num_list = []
    for num in range(2, n + 1):
        flag1 = True
        for j in range(2, int(math.sqrt(num) + 1)): # Try divide 2 to sqrt(num)
            flag2= True
            ### check whether j is a prime, if j is not a prime, continue,
            # because if the number can be divided by a not prime, it must can be divided by the prime
            # number between 2~10 i.e. 2,3,5,7###
            for k in range(2, int(math.sqrt(j) + 1)):
                if (j % k == 0):
                    flag2 = False # j is not a prime
                break
            if(not flag2):
                continue
            ### check whether j is a prime ###
            
            if(num % j==0): # j is a prime
                flag1=False # num is not a prime
                break
        if (flag1):
            pri_num_list.append(num)
    print(len(pri_num_list), pri_num_list)

if __name__ == "__main__":
    generate_prime()
    generate_prime1()
    generate_prime2()
    generate_prime3()