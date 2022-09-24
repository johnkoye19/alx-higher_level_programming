#!/usr/bin/python3
# Write a function that prints a matrix of integers.


def print_matrix_integer(matrix=[[]]):
    # Read through the matrix[][]
    for i in matrix:
        for a in i:
            # then print
            print("{:d}".format(a), end=" ")
        # newline
        print()
