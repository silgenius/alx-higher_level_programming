#!/usr/bin/python3

from models.rectangle import Rectangle

"""
    Class: Square

    Represents a square, inheriting from the Rectangle class.
"""


class Square(Rectangle):
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

        return("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width, self.height))
    
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
