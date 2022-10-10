#!/usr/bin/python3
# write a function that prints integers only


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
