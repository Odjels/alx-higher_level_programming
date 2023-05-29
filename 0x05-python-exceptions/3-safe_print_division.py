#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div_value = a / b
    except ZeroDivisionError:
        div_value = "None"
        return None
    finally:
        print("Inside result: {}".format(div_value)
    return div_value
