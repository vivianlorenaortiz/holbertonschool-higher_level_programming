#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        nw = chr(ord(str[i]))
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            nw = chr(ord(str[i]) - 32)
        print("{}".format(nw), end="")
    print()
