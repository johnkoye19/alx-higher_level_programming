#!/usr/bin/python3
# we are trying to fetch a website using urllib

import urllib.request

if __name__ = "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as task0:
        # print (type(task0))
        # actual type
        print ("Body response:")
        actual_type = task0.read()
        print ("\t- type: ", type(actual_type))
        # actual content
        print ("\t- content: ", actual_type)
        # print string representation
        string_type = actual_type.decode()
        print ("\t- utf8 content: ", string_type)
