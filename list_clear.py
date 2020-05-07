if __name__=="__main__":
    lst1 = [1, 2, 3]
    lst2 = lst1 ##### pass by reference
    lst3 = lst1.copy()
    # del lst1[:]
    lst1.clear() ###### the same effect as del lst1[:]
    print("lst1",lst1) #[]
    print("lst2",lst2) ######[] pass by reference
    print("lst3",lst3) #[1,2,3]
    del lst1
    try:
        print(lst1) # error: name 'lst1' is not defined
    except:
        print("error")
    print("lst2",lst2) ##############[]
    print("lst3",lst3) #[1,2,3]
    del lst2
    try:
        print(lst2)  # error: name 'lst2' is not defined
    except:
        print("error")
    del lst3
    try:
        print(lst3)  # error: name 'lst3' is not defined
    except:
        print("error")

    l1=[1,2,3]
    l2=[1,2,3]
    l3=[3,2,1]
    print(l1==l2)
    print(l1==l3)
