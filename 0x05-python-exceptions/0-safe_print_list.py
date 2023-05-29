#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for b in range(0, x):
            print(f"{my_list[b]}", end="")
            num += 1
    except Exception:
        print()
        return num
    print()
    return num
