#!/usr/bin/python3
# Write a function that divides 2 integers and prints the result.


def safe_print_division(a, b):
    try:
        c = a / b
        # print("{}".format(c))
        return (c)
    except (ZeroDivisionError):
        # print("{}".format(None))
        return (None)
    finally:
        if (b != 0):
            print("Inside result: {}".format(c))
        else:
            print("Inside result: {}".format(None))
