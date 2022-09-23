#!/usr/bin/python3
# Write a function that prints all integers of a list, in reverse order.

def print_reversed_list_integer(my_list=[]):
    a = -1
    for i in range(len(my_list)):
        print("{}".format(my_list[a]))
        a = a - 1
