#!/usr/bin/python3
j = 0
while (j < 10):
    i = j + 1
    while (i < 10):
        if (i < 10 or j < 10):
            print("{:01d}{:01d}".format(j, i), end=", ")
        i = i + 1
    j = j + 1
