#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    num = my_list[0]
    for a in range(0, len(my_list)):
        if my_list[a] > num:
            num = my_list[a]
    return num
