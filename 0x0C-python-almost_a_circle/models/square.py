#!/usr/bin/python3

"""
Module: square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class: Square

    Represents a square, inheriting from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance with size, x, y, and id.
        Calls the super class with id, x, y, width, and height.

        Note: width and height are assigned the value of size.
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square instance.

        Returns:
        - str: A string representation in the format:
          "[Square] (<id>) <x>/<y> - <size>".
        """

        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
        - int: The size of the square.
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Parameters:
        - value (int): The new value for the size attribute.
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns each argument to the corresponding attribute.

        Parameters:
        - *args: Variable number of arguments representing id, width,
        height, x, and y attributes.
        """

        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
        - dict: A dictionary containing the id, width, height, x, and
        y attributes.
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.height,
            'y': self.y,
            }
