def add_func(list1: list, list2: list):
    #eng kichik va katta uzunlikdagi listlarni aniqlash
    if len(list1) < len(list2):
        mini_list = list1
        max_list = list2
    else:
        mini_list = list2
        max_list = list1

    a1, b1 = "", ""
    for i in mini_list: a1 += str(i)
    for b in max_list[0:len(mini_list)]: b1 += str(b)

    return int(a1)+int(b1)


add_func(list1=[2,7,0,1], list2=[1,0,7,2])
