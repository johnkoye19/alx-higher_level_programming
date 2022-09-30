#!/usr/bin/python3
# Write a function that returns a
# key with the biggest integer value


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    
    m = list(a_dictionary.values())
    ma = m[0]
    for i in m:
        if i > ma:
            ma = i
    for x in a_dictionary.keys():
        if a_dictionary[x] == ma:
            return (x)
