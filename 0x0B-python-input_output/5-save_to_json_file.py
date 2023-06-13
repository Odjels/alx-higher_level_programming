#!/usr/bin/python3
""" module for task 5 """


import json


def save_to_json_file(my_obj, filename):
    """ save an object to file """
    with open(filename, mode="w", encoding="utf-8") as f:
        dt = json.dump(my_obj, f)
        return dt
