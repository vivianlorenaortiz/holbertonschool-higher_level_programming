#!/usr/bin/Python3
"""
this function that prints a string line.
"""


def say_my_name(first_name, last_name=""):
    """
    print name of the function.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {}{}".format(first_name,  last_name))
