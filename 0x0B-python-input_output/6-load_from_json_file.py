#!/usr/bin/python3
""" creating object from a json file """


import json


def load_from_json_file(filename):
    """ return the data from the json file """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
