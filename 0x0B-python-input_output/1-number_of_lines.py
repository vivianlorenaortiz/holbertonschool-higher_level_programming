#!/usr/bin/python3
"""  function that returns the number of lines of a text file: """


def number_of_lines(filename=""):
    """returns the number of lines of a text file: """
    with open(filename, mode="r", encoding="utf-8") as myFile:

        return(len(myFile.readlines()))
