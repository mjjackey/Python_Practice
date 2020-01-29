lst1 = [1, 2, 3]
lst2 = lst1
del lst1[:]
print(lst2) #[]
del lst1
# print(lst1) # error: name 'lst1' is not defined
print(lst2) #[]
del lst2
print(lst2)  # error: name 'lst2' is not defined