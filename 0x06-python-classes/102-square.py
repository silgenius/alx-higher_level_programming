#!/usr/bin/python3

"""
    A module for a class square
"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Parameters:
        - size: A number (int or float) representing
        the size of the square (default is 0).

        Raises:
        - TypeError: If the provided size is not
        a number (neither int nor float).
        - ValueError: If the provided size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        - value: A number (int or float) representing
        the size of the square.

        Raises:
        - TypeError: If the provided value is not a number
        (neither int nor float).
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Formula: size^2

        Returns:
        - float or int: The calculated area of the square.
        """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """
        Overrides the equality operator (==) for Square instances.

        Returns True if the areas of the two
        squares are equal, False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if areas are equal, False otherwise.
        """
        return (self.area() == other.area())

    def __ne__(self, other):
        """
        Overrides the not equal operator (!=) for Square instances.

        Returns True if the areas of the two
        squares are not equal, False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if areas are not equal, False otherwise.
        """
        return (self.area() != other.area())

    def __gt__(self, other):
        """
        Overrides the greater than operator (>) for Square instances.

        Returns True if the area of the current square
        is greater than the area of the other square, False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if the area is greater, False otherwise.
        """
        return (self.area() > other.area())

    def __ge__(self, other):
        """
        Overrides the greater than or equal to operator
        (>=) for Square instances.

        Returns True if the area of the current
        square is greater than or equal to
        the area of the other square, False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if the area is greater
        than or equal, False otherwise.
        """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """
        Overrides the less than operator (<) for Square instances.

        Returns True if the area of the current square is
        less than the area of the other square, False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if the area is less, False otherwise.
        """
        return (self.area() < other.area())

    def __le__(self, other):
        """
        Overrides the less than or equal to operator (<=) for Square instances.

        Returns True if the area of the current square is
        less than or equal to the area of the other square,
        False otherwise.

        Parameters:
        - other: Another Square instance for comparison.

        Returns:
        - bool: True if the area is less than or equal, False otherwise.
        """
        return (self.area() <= other.area())
