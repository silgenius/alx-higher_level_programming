#!/usr/bin/python3

"""
This module defines a class Rectangle representing a geometric rectangle.
It includes methods to set and retrieve the width and height of the rectangle.
"""


class Rectangle:
    """
    Represents a geometric rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Parameters:

            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        Raises:

        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Getter method for retrieving the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for setting the width of the rectangle.

        Parameters:
            value (int): The new width value.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for retrieving the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for setting the height of the rectangle.

        Parameters:
            value (int): The new height value.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
