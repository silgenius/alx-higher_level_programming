#!/usr/bin/python3

"""
Module: square_printer

Provides a function to print a square made of '#'
characters with a specified size.

Functions:
- print_square(size): Prints a square with the given size.

"""

def print_square(size):
    """
    Prints a square made of '#' characters with the specified size.

    Parameters:
    - size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer or if
    size is a float and less than 0.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
