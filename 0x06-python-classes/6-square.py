#!/usr/bin/python3

"""
    A module for a class square
"""


class Square:
    """
    A class to represent a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the Square.
            Position (tuple): The position of the Square.

        Raises:
            TypeError: If size is not an integer /
            not tuple for position.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2\
 positive integers")
        for i in range(2):
            if not isinstance(position[i], int):
                raise TypeError("position must be a tuple of 2\
 positive integers")
            if position[i] < 0:
                raise TypeError("position must be a tuple of 2\
 positive integers")
        self.__position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            int: The position of the square.
        """
        return (self.__position)

    @position.setter
    def size(self, value):
        """
        Sets value as the position of the square.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        for i in range(self.__position[1]):
            if self.position[1] == 0:
                break
            print()

        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
