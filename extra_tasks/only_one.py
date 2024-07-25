def only_one(list1: list):
    for i in list1:
        if list1.count(i) == 1:
            print(i)


only_one(list1=[2, 2, 1, 1, 5, 5, 3, 3, 6, 6, 9, 9, 4])

