#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div_value = a / b
    except ZeroDivisionError:
        div_value = "None"
        print("You cant divide by zero")
        return None
    finally:
        print("Inside result: {}".format(res))
    return div_value
