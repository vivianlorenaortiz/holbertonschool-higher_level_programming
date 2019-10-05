#!/usr/bin/python3
"""
Funtion that prints a square with the character #.
"""


def print_square(size):
    """
    Function print square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(size * "#")
