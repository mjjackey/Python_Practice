"""
Accept a line of string set split by comma, the number of string <1000, pick the un-repeated prime number,
sort ascending,output them; if no prime number,output "empty"
"""
import math
def fun():
    input_num_list=list(map(int,input().strip().split(',')))
    out=set()
    for num in input_num_list:
        if(all(num%i !=0 for i in range(2,int(math.sqrt(num))+1))):
            ##### Return True if all elements of the iterable are true (or if the iterable is empty)
            ##### So, if the input_num_list is {1,2}, the result is wrong
            out.add(num)
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
        if(all(num%i !=0 for i in range(2,int(math.sqrt(num))+1))):
            out.append(num)
    out=sorted(set(out))
    if(len(out)==0):
        print("empty")
    else:
        for num in out:
            print(num)

if __name__ == "__main__":
    fun()