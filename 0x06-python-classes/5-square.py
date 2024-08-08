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
        Initialize a Square object.

        Args:
            size (int): The size of the Square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets value as the size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints the square with the character '#'.

        This method prints a visual representation of the square object.
        It uses the '#' character to represent each unit of the square's size.

        Returns:
            None
        """

        if self.__size == 0:
            print()
        else:
            i = 0
            while i != self.__size:
                print("#" * self.__size, end="")
                print()
                i += 1
