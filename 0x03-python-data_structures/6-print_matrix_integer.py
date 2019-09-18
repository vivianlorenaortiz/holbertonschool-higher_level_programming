#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        return
    for element in matrix:
        if (len(element)-1) < 0:
            continue
        for i in range(len(element)-1):
            print("{:d}".format(element[i]), end=" ")

        print("{:d}".format(element[(len(element)-1)]))
