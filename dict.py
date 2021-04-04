if __name__ == "__main__":
    x = {'a':1, 'b': 2}
    y = {'b':10, 'c': 11}
    z = x.copy()
    z.update(y)
    z.update(d=5)  # default for string 'd'
    z['e']=8
    print(z)

    list_value=[12,13,14,15,16]
    # list_key=[i for i in range(len(list_value))]
    for i in range(len(list_value)):
        z[i]=list_value[i]
    print(z)

    """
    Purpose: find the the index provided the value 10
    Get the key provided by the value
    for a dictionary, key is the unique, whereas value is not, 
    so dictionary is one vs one, multiple vs one, rather than one vs multiple
    """
    key=list(z.keys())[list(z.values()).index(10)]
    print(key)

    def getKey(dict,value):
        """
        :param dict:
        :param value:
        :return: a list [key]
        """
        key=[k for k,v in dict.items() if v==value]
        return key

    print(getKey(z,10))

    """
    This is invalid for the condition that the original dictionary is multiple vs one
    """
    new_dict={v:k for k,v in z.items()}
    print(new_dict[10])

