#1. batched
from itertools import batched
numbers: list[int]=[1,2,3,4,5,6,7]
my_batch: batched=batched(numbers,n=3)
print(list(my_batch))
my_batch2: batched=batched(numbers,n=2)
print(next(my_batch2))
print(next(my_batch2))

#2. zip_longest()
from itertools import zip_longest
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]
for name, age in zip_longest(names, ages, fillvalue="N/A"):
    print(f"{name}: {age}")
# Output:
# Alice: 25
# Bob: 30
# Charlie: N/A

#3. product()
from itertools import product
elements:list[str]=['A','B','C']
my_product:product=product(elements,repeat=3)
for t in my_product:
    print(''.join(t))  # Output all combinations of three characters

#4. starmap()
from itertools import starmap
# 定义一个函数
def multiply(a, b):
    return a * b
# 使用生成器作为输入
data = ((i, i + 1) for i in range(5))
result = starmap(multiply, data)
print(list(result))  # 输出: [0, 2, 6, 12, 20]

# 使用 map
data = [(1, 2), (3, 4)]
result = map(lambda x: x[0] + x[1], data)
print(list(result))  # 输出: [3, 7]

# Use starmap
result = starmap(lambda a, b: a + b, data)
print(list(result))  # 输出: [3, 7]

#5. groupby()
from itertools import groupby
def count_vowels(word:str)->int:
    """
    Make a statics of word containing vowels
    :param word:
    :return: The number of vowel letters
    """
    vowel_count:int=0

    for letter in word:
        if letter in 'aeiouAEIOU':
            vowel_count+=1

    return vowel_count

words:list[str]=['cat','dog','mood','banana','red','hood','mate']
sorted_words: list[str] = sorted(words,key=count_vowels)
grouped:groupby=groupby(sorted_words,key=count_vowels)

for vowels, grouped_words in grouped:
    print(f'{vowels=} {list(grouped_words)}')

# cycle
from itertools import cycle
for i, char in zip(range(5), cycle("AB")):
    print(i,char)  # 输出 A, B, A, B, A

# repeat
from itertools import repeat
exponent:int= repeat(2)
squares = map(pow, range(5), exponent)  # 计算 0², 1², 2², 3², 4²
print(list(squares))

# isslice
# This creates a new list in memory.
data = list(range(10))
print(data[2:8])  # Output: [2, 3, 4, 5, 6, 7]

# This does not create a new list in memory, making it more memory-efficient.
from itertools import islice
result = islice(range(10), 2, 8)
print(list(result))  # Output: [2, 3, 4, 5, 6, 7]

