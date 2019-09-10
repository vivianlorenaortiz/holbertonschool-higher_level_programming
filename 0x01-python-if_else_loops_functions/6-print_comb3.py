#!/usr/bin/python3
j = 0
while (j < 10):
    i = j + 1
    while (i < 10):
        if (j != 8):
            print("{:01d}{:01d}".format(j, i), end=", ")
        else:
            print("{:01d}{:01d}".format(j, i))
        i = i + 1
    j = j + 1
