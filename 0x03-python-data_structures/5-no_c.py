#!/usr/bin/python3
# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    new = ''
    for i in my_string:
        if (i == 'c') | (i == 'C'):
            i = ''
        new = new + i
    return(new)
