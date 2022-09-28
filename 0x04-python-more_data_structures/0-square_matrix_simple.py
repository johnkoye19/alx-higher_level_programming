#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.


def square_matrix_simple(matrix=[]):
    # new list
    new = []
    # square each element
    for i in matrix:
        new.append([x**2 for x in i])
    # return new list
    return new
