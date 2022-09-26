#!/usr/bin/python3
# Write a function that finds the biggest integer of a list.


def max_integer(my_list=[]):
    # list is empty, return None
    if len(my_list) == 0:
        return None
    # list haas just one element
    if len(my_list) == 1:
        return my_list[0]
    # for max
    var = my_list[0]
    # read through the list
    for i in my_list:
        if i > var:
            var = i
    # if the next num is >
    # var take its value
    return var
