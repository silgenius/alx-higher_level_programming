#!/usr/bin/python3

"""
This module defines a class Rectangle representing a geometric rectangle.
It includes methods to set and retrieve the width and height of the rectangle.
"""


class Rectangle:
    """
    Represents a geometric rectangle.
    """

    number_of_instances = 0

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
        type(self).number_of_instances += 1

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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """

        return (self.__height * self.__width)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle using
        # characters, forming a rectangular shape.

        Returns:
            str: The string representation of the rectangle
        """

        if self.__height == 0 or self.__width == 0:
            return ""

        rectangle_string = ""
        for _ in range(self.__height):
            rectangle_string += "#" * self.__width + "\n"
        return rectangle_string[:-1]

    def __repr__(self):
        """
        Returns a string representation of the Rectangle instance.

        The representation includes the values of
        the height and width attributes.

        Returns:
            str: A string representation of the Rectangle instance.
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes a Rectangle instance and prints a farewell message.

        The method is automatically called when the instance
        is about to be destroyed.

        Prints:
            str: A farewell message indicating the
            deletion of the Rectangle instance.
        """

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
