#!/usr/bin/python3
# Write a function that adds all unique integers
# in a list (only once for each integer).


def uniq_add(my_list=[]):
    # we will check the occurence of each element
    # then add, if applicable
    total = 0
    new = set()
    for i in my_list:
        new.add(i)
        x = my_list.count(i)
        if x == 1:
            total = total + i
    return (sum(new))
