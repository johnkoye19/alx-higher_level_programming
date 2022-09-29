#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.


def print_sorted_dictionary(a_dictionary):
	for i in sorted(a_dictionary.keys()):
		print("{:s}: {}".format(i, a_dictionary[i]))
