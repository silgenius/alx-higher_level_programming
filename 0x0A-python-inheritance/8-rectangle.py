#!/usr/bin/python3

"""
Module: 7-rectangle

This module defines a Rectangle class that
inherits from the BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class: Rectangle

    Represents a rectangle with width and height,
    inheriting from the BaseGeometry class.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a new
    rectangle with the given width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a new rectangle with the given width and height.

        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.

        Raises:
        - TypeError: If either width or height is not a positive integer.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
