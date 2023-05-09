#!/usr/bin/python3


def print_last_digit(number):
    if number > 0:
        number = number % 10
    else:
        number = ((-1) * numbe)r % 10

    print("{:d}".format(number), end="")
    return number
