#!/usr/bin/python3

def no_c(my_string):
    s = len(my_string)
    bab = ""
    for a in range(0, s):
        if my_string[a] == "c" or my_string[a] == "C":
            continue
        bab = bab + my_string[a]
    return bab
