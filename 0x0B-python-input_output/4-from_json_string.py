#!/usr/bin/python3
""" module forb task 4 """


import json


def from_json_string(my_str):
    """ convert json file to python dict """
    return json.loads(my_str)
