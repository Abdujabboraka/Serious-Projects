def funckiy(list1: list):
    unique = list(set(list1))
    for i in range(len(list1)-len(unique)):
        unique.append("_")
    return unique

