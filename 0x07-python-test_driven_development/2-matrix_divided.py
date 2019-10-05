#!/usr/bin/python3

"""
Function that divides all elements of a matrix,must be alist of integers
or floats, otherwise raise a TypeError exception with a specific error.
Div must be a number (integer or float),otherwise raise a TypeError exception.
"""


def matrix_divided(matrix, div):
    """
    All elements of the matrix should be divided by div,rounded to 2 decimal.
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    new_mtx2 = [x[:] for x in matrix]
    sz = len(matrix[0])
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if sz != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int\
               and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")
            new_mtx2[i][j] = round(matrix[i][j] / div, 2)
    return new_mtx2
