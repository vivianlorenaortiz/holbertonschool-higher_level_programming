#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    lg = len(argv) - 1
    if lg == 0:
        print("{}".format("0 arguments."))
    elif lg == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(lg, "arguments:"))
        for i in range(1, lg + 1):
            print("{:d}: {}".format(i, argv[i]))
