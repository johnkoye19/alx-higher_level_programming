#!/usr/bin/python3
# Write a function that replaces an element in a list at a specific
# position without modifying the original list (like in C).
def new_in_list(my_list, idx, element):
    copy = []
    for i in my_list:
        copy.append(i)
    if idx < 0:
        return copy
    if idx > (len(my_list) - 1):
        return copy
    copy[idx] = element
    return copy
