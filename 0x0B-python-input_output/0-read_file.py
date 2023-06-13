#!/usr/bin/python3
""" module for reading files """


def read_file(filename=""):
    """ read text files """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
