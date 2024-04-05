#!/usr/bin/python3

"""
    A module for a class square
"""


class Square:
    """
    A simple class representing a square

    Attributes:
        - size: The size of each side of the square.
    """

    def __init__(self, size):
        """
        Initializes a new square with the given side length.

        Parameters:
            - size: The size of each side of the square.
        """
        self.__size = size
