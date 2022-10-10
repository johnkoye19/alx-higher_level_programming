#!/usr/bin/python3
# write a function that prints x elements of a list


def safe_print_list(my_list = [], x = 0):
    n = 0
    try:
        for i in range(x):
            print(my_list[i], end = "")
            n = n + 1
        print("\n", end = "")
    except IndexError:
        print("\n", end = "")
        return (n)
    return (n)
