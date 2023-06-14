#!/usr/bin/python3
""" json string to object """


import json


def from_json_string(my_str):
    """ converting a json file to python dict """
    return json.loads(my_str)
