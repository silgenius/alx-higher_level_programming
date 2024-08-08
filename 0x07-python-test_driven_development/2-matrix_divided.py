#!/usr/bin/python3

"""
A matrix module that divides a matrix by a value
given to it
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided, containing integers or floats.
    - div (int or float): The divisor to divide all elements of the matrix by.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places after division.

    Raises:
    TypeError: If the matrix is not a list of lists of integers or floats.
               If each row of the matrix does not have the same size.
               If the divisor is not a number (integer or float).

    ZeroDivisionError: If the divisor is equal to 0.
    """

    for row in matrix:
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
