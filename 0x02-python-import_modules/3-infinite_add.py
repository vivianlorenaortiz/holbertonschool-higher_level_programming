#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    lg = len(argv)
    addition = 0
    for i in range(1, lg):
        addition += int(argv[i])
    print("{:d}".format(addition))
