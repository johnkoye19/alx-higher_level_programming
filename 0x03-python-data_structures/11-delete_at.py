#!/usr/bin/python3
# Write a function that deletes the item at a specific position in a list.


def delete_at(my_list=[], idx=0):
    # If idx is negative or out of range(returns the same list)
    if idx < 0:
        return my_list
    if (idx > (len(my_list) - 1)):
        return my_list
    del my_list[idx]
    return my_list
