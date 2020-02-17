"""
Accept a line of string set split by comma, the number of string <1000, pick the un-repeated prime number,
sort ascending,output them; if no prime number,output "empty"
e.g.
1,2,3,3,5,7,9
"""
import math
def fun():
    input_num_list=list(map(int,input().strip().split(',')))
    out=set()
    for num in input_num_list:
        # if(num !=1 and all(num%i !=0 for i in range(2,int(math.sqrt(num))+1))):
        #     ##### all Return True if all elements of the iterable are true (or if the iterable is empty)
        #     ##### So, if the input_num_list contain {1}, the loop does not do, the result is wrong
        #     ##### Actually, for num=2 or num=3, inner loop does not do either, but 2,3 are prime
        # out.add(num)
        flag= True
        for i in range(2,int(math.sqrt(num))+1):
            if (num%i==0):
                flag= False
                break
        if(flag and num!=1): out.add(num)

    out=sorted(out)
    if(len(out)==0):
        print("empty")
    else:
        for num in out:
            print(num)

def fun2():
    input_num_list=list(map(int,input().strip().split(',')))
    out=[]
    for num in input_num_list:
        if(num !=1 and all(num%i !=0 for i in range(2,int(math.sqrt(num))+1))):
            out.append(num)
    out=sorted(set(out))
    if(len(out)==0):
        print("empty")
    else:
        for num in out:
            print(num)

if __name__ == "__main__":
    fun()