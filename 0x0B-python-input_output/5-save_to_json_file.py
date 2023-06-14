#!/usr/bin/python3
""" saving object """


import json


def save_to_json_file(my_obj, filename):
    """ saving an object to a file """
    with open(filename, mode="w", encoding="utf-8") as f:
        dt = json.dump(my_obj, f)
        return dt
