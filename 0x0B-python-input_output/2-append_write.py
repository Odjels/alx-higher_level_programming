#!/usr/bin/python3
""" append to a file """


def append_write(filename="", text=""):
    """ adding to the end of the line """
    with open(filename, mode="a", encoding="utf-8") as f:
        sos = f.write(text)
        return sos
