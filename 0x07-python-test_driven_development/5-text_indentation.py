#!/usr/bin/python3
"""
function that prints a text with 2 new lines after each of these character., ?.
"""


def text_indentation(text):
    """
    text must be a string, otherwise raise a TypeError with a exception.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
                if text[i] == " " and text[i-1] in ".?:":
                    print("\n")
                else:
                    print(text[i], end="")
