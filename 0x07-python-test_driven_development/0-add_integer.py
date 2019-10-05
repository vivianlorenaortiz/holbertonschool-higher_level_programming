#!/usr/bin/python3
"""
Function that adds 2 integers a and b must be integers or floats,
otherwise raise a TypeError exception with the message a must be a  integer
or b musdt be an integer.
"""


def add_integer(a, b=98):
    """
    Returns an integer:the addition of a and b.
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    elif isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return(int(a) + int(b))
