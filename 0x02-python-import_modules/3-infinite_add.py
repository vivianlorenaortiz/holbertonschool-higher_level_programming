#!/usr/bin/python
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    addition = 0
    for i in range(1, 1):
        addition += int(argv[i])
    print("{:d}".format(addition))
