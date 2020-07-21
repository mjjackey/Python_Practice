import math
def root(n,num):
    incre=0.005
    i=1
    while(i<num):
        prod=1
        for j in range(n): # i multiply n times
            prod=prod*i
        if(prod>=num):
            n_root=i-incre
            break
        i+=incre
    print(n_root)

def root2(n,num):
    n_root=math.exp(1/n * math.log(num))
    print(n_root)

def root3(n,num):
    acc=0.001
    # if(num>=1):
    #     low=1
    #     high=num
    # else:
    #     low=num
    #     high=1
    low=0
    high=num
    while(abs(low-high)>=10**-16):
        mid=(low+high)/2.0
        # prod=1
        # for j in range(n): # mid multiply n times
        #     prod=prod*mid
        prod=mid**n
        if(abs(prod-num)<=acc):
            break
        if(prod>=num): high=mid
        else: low=mid

    print("%.12f"%mid)

if __name__ == "__main__":
    num,n=map(int,input().strip().split())
    root3(n,num)
