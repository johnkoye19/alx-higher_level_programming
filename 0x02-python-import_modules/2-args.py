#!/usr/bin/python3
if __name__ == "__main__":
    import sys
ac = len(sys.argv)
if ac == 2:
    print("1 argument:")
elif ac == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(ac -1))
if ac > 1:
    for i in range(1, ac):
        print("{}: {}".format(i, sys.argv[i]))
