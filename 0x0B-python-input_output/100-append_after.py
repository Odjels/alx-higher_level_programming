#!/usr/bin/python3

"""search and append"""


def append_after(filename="", search_string="", new_string=""):
    """Inserting a text after each line """
    text_line = ""
    with open(filename) as r:
        for line in r:
            text_line += line
            if search_string in line:
                text_line += new_string
    with open(filename, "w") as w:
        w.write(text_line)
