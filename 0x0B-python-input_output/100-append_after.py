#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    """
    text_line = ""
    with open(filename) as r:
        for line in r:
            text_line += line
            if search_string in line:
                text_line += new_string
    with open(filename, "w") as w:
        w.write(text_line)
