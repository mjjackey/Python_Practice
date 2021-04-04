if __name__ == "__main__":
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(list(enumerate(seasons)))
    #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    print(list(enumerate(seasons, start=1)))
    # 下标从 1 开始 [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

    seq = ['one', 'two', 'three']
    for i, element in enumerate(seq):
        print(i, element)