#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        j = 0
        for i in row:
            print("{:d}".format(i), end="")
            if j < len(row) - 1:
                print(" ", end="")
                j += 1
        print()
