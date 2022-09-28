#!/usr/bin/python3
# Write a function that replaces all
# occurrences of an element by another in a new list.


def search_replace(my_list, search, replace):
    # my_list is the initial list
    # search is the element to replace in the list
    # replace is the new element
    # You are not allowed to import any module
    # new list
    new = []
    # read through
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new
