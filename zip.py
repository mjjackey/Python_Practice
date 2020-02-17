"""
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
"""
nums = ['flower','flow','flight'] # each string is regarded as a tuple
for i in zip(*nums):
    print(i)

"""
The list elements are connected in sequence
"""
l = ['a', 'b', 'c', 'd', 'e','f']
print(l)
print(list(zip(l[:-1],l[1:])))
