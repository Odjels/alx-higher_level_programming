#!/usr/bin/python3
""" writing text """


def write_file(filename="", text=""):
    """ writing the text to a file """
    with open(filename, encoding="utf-8", mode="w") as f:
        n_o_c = f.write(text)
        return n_o_c
