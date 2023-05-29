#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
     my_new_list = []
    for b in range(0, list_length):
        try:
            div = my_list_1[b] / my_list_2[b]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            my_new_list.append(div)
    return (my_new_list)
