#!/usr/bin/python3
""" module for task 6 """


import json


def load_from_json_file(filename):
    """ return data from json file """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
