#!/usr/bin/python3

"""Retriving an element from a list."""

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
