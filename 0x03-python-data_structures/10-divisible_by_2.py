#!/usr/bin/python3

def divisible_by_2(my_list=[]):
      bab = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            bab.append(True)
        else:
            bab.append(False)

    return (bab)
