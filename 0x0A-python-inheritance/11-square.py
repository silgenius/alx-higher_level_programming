#!/usr/bin/python3

"""
Module: square_module

This module defines a Square class that
inherits from the Rectangle class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class: Square

    Represents a square, inheriting from the Rectangle class.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new square with the given size.

        Parameters:
        - size: The size of the square.
        """

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the rectangle.
        """

        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
