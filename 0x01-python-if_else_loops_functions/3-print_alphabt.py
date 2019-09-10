#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if chr(alpha) is not "q" and chr(alpha) is not "e":
        print("{:s}".format(chr(alpha)), end="")
