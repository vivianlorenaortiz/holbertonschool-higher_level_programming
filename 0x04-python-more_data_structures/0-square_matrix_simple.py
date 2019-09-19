#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = []
    for i in matrix:
        nw_matrix.append(list(map(lambda x: x**2, i)))
        return nw_matrix
