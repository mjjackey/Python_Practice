class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # return an iterator
        return iter(self.data)


class MyIterable2:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        # return an item with the index
        return self.data[index]



class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


if __name__=='__main__':
    my_obj = MyIterable([1, 2, 3, 4])
    for item in my_obj:
        print(item)

    my_obj2 = MyIterable2([1, 2, 3, 4])
    for item in my_obj2:
        print(item)

    my_obj = MyIterator([1, 2, 3, 4])
    for item in my_obj:
        print(item)



