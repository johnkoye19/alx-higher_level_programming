#!/usr/bin/python3
if __name__ == "__main__":
    import sys
ac = len(sys.argv)
if ac == 2:
    print("{:d} argument:".format(ac - 1))
elif ac == 1:
    print("{:d} arguments.".format(ac -1))
else:
    print("{:d} arguments:".format(ac -1))
if ac > 1:
    for i in range(1, ac):
        print("{:d}: {}".format(i, sys.argv[i]))
