#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    case = len(my_list) - 1)
    if idx < 0 or idx >= case:
        return (my_list)
    
    bab = my_list.copy()
    bab[idx] = element
    return (bab)

