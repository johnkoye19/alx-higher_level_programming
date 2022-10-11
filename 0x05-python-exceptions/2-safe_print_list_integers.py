#!/usr/bin/python3
# Write a function that prints the first x elements of a list and only integers.


def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n = n + 1
        except(ValueError, TypeError):
            continue
        # except(IndexError):
            # break
    print("\n", end="")
    return(n)
