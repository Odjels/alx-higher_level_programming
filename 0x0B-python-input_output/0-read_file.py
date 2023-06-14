#!/usr/bin/python3
"""reading files """


def read_file(filename=""):
    """ reading the text files """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
