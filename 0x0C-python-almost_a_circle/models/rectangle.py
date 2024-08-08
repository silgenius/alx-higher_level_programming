#!/usr/bin/python3

"""
    Class: Rectangle

    Represents a rectangle with width, height, x, and y
    attributes, inheriting from the Base class.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    - __x (int): The x-coordinate of the top-left corner of the rectangle.
    - __y (int): The y-coordinate of the top-left corner of the rectangle.
    - id (int): An identifier for the rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """
    Class: Rectangle

    Represents a rectangle with private instance
    attributes and public getter and setter methods.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with width, height, x, and y.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        - int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Parameters:
        - value (int): The new value for the width attribute.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
        - int: The height of the rectangle.
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Parameters:
        - value (int): The new value for the height attribute.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
        - int: The x-coordinate of the top-left corner of the rectangle.
        """

        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Parameters:
        - value (int): The new value for the x attribute.
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
        - int: The y-coordinate of the top-left corner of the rectangle.
        """

        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Parameters:
        - value (int): The new value for the y attribute.
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - int: The area of the rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Displays the rectangle using '#' characters,
        respecting the x and y coordinates.
        Prints leading spaces based on the x and y attributes.
        """

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """

        return (
                "[Rectangle] ({}) {}/{} - {}/{}"
                .format(
                    self.id,
                    self.__x,
                    self.__y,
                    self.__width,
                    self.__height
                    )
                )

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
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
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
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
