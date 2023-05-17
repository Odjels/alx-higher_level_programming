#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    current_set = set_2.difference(set_1)
    current_set.update(set_1.difference(set_2))
    return current_set
