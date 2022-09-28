#!/usr/bin/python3
# Write a function that returns a set of common elements in two sets

def common_elements(set_1, set_2):
    new = set_1.intersection(set_2)
    return new
