"""
Based on the given integer n, list, return the element whose  frequency of occurrence
is equal to n, the time complexity must less O(nlogn)
"""
class Rare:
    def nth_most_rare(elements,n):
        if(not isinstance(elements,list)):
            print("not list")
            return
        if(not isinstance(n,int)):
            print("not int")
            return
        x={}
        for ele in elements:
            if str(ele) not in x.keys():  # use str,because ele is a variable
                x.update({str(ele):1})  # str
            else:
                x[str(ele)] += 1
            # print(x)
        element=list(x.keys())[list(x.values()).index(n+1)]
        return element

if __name__ == "__main__":
    n=Rare.nth_most_rare([5,4,3,2,1,5,4,3,2,5,4,3,5,4,5],4)
    print(n)

    n=Rare.nth_most_rare((5,4,3,2,1,5,4,3,2,5,4,3,5,4,5),4)
    print(n)

    n=Rare.nth_most_rare([5,4,3,2,1,5,4,3,2,5,4,3,5,4,5],4.5)
    print(n)