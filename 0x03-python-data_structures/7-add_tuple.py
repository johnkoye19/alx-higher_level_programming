#!/usr/bin/python3
# Write a function that adds 2 tuples.


def add_tuple(tuple_a=(), tuple_b=()):
    # add first elements
    if (len(tuple_a) == 1):
        c = 0
        d = tuple_a[0]
    elif (len(tuple_a) == 0):
        c = 0
        d = 0
    else:
        c = tuple_a[1]
        d = tuple_a[0]
    if (len(tuple_b) == 1):
        e = 0
        f = tuple_b[0]
    elif (len(tuple_a) == 0):
        e = 0
        d = 0
    else:
        e = tuple_a[1]
        f = tuple_a[0]
    # the new tuple
    a = d + f
    b = c + e
    tuple_c = (a, b)
    return(tuple_c)
