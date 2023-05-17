#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        bab = 0
        flab = 0
        average = 0
        for a in range(len(my_list)):
            for b in range(len(my_list[a])):
                bab += my_list[a][0] * my_list[a][1]
                flab += my_list[a][1]
        average = bab / flab
        return average
    return 0
