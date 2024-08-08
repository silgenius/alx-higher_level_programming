#!/usr/bin/python3

"""
Module: pascal_triangle_module

This module provides a function for generating
Pascal's triangle up to the specified level.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified level.

    Parameters:
    - n (int): The level up to which Pascal's triangle should be generated.

    Returns:
    - list of lists: A list of lists of integers
    representing Pascal's triangle.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]

    pascal = [[1], [1, 1]]

    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
        row.append(1)
        pascal.append(row)

    return pascal
