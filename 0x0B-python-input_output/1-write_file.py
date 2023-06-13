#!/usr/bin/python3
""" module for writing text """


def write_file(filename="", text=""):
    """ write text to a file """
    with open(filename, encoding="utf-8", mode="w") as f:
        number_of_characters = f.write(text)
        return number_of_characters
