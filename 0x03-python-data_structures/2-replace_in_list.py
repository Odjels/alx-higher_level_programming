#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    bab = len(my_list)

    if idx < 0 and idx >= bab:
        return my_list
    else:
        my_list[idx] = element
        return my_list
