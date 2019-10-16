#!/usr/bin/python
"""  function that returns the number of lines of a text file: """


def number_of_lines(filename=""):
    """returns the number of lines of a text file: """
    cont = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cont += 1
    return cont
