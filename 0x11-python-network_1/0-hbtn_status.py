#!/usr/bin/python3
"""we are trying to fetch a website using urllib"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as t0:
        # print (type(t0))
        # actual type
        print("Body response:")
        actual_type = t0.read()
        print("\t- type: ", type(actual_type))
        # actual content
        print("\t- content: ", actual_type)
        # print string representation
        string_type = actual_type.decode()
        print("\t- utf8 content: ", string_type)
