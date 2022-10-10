#!/usr/bin/python3
# Write a function that prints the first x elements of a list and only integers.


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]))
            n = n + 1
        print("\n")
        return (n)
    except (ValueError, TypeError):
        continue
