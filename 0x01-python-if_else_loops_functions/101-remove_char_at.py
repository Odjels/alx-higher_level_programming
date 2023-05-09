#!/usr/bin/python3


def remove_char_at(str, n):
    a = ""
    if n > 0:
        a = (str[:n] + str[n+1])
        return (a)
    else n < 0:
        return (str)

