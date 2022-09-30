#!/usr/bin/python3
# Write a function that returns a new
# dictionary with all values multiplied by 2


def multiply_by_2(a_dictionary):
    new = dict()
    for x in a_dictionary.keys():
        new[x] = a_dictionary[x] * 2
    return (new)
