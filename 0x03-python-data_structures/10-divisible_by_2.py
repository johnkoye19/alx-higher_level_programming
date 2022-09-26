#!/usr/bin/pyhton3
# Write a function that finds all multiples of 2 in a list.


def divisible_by_2(my_list=[]):
    new_list = []
    # read through my_list
    for i in my_list:
        # check if i is divisible by 2
        new_list.append(i % 2 == 0)
    return new_list
