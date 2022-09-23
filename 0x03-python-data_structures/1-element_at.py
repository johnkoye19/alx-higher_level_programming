#!/usr/bin/python3
# Write a function that retrieves an elemenfrom a list like in C.

def element_at(my_list, idx):
    if idx < 0:
        return None
    if (len(my_list) - 1) < idx:
        return None
    return(my_list[idx])
