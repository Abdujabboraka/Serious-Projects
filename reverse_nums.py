def isreverse(num: int):
    #checking...
    reversed_num = str(num)[::-1]
    if reversed_num == str(num):
        return True
    else:
        return False


isreverse(num=122)
