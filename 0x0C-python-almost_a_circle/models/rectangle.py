#!/usr/bin/python3

Base = __import__ ('base').Base


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(self, id)

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
        - int: The width of the rectangle.
        """

        return self.__width

    @width.setter
    def width(self. value):
        """
        Setter for the width attribute.

        Parameters:
        - value (int): The new value for the width attribute.
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
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
    def heigth(self, value):
        """
        Setter for the height attribute.

        Parameters:
        - value (int): The new value for the height attribute.
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
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

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
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

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
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
        Displays the rectangle using '#' characters, respecting the x and y coordinates.
        Prints leading spaces based on the x and y attributes.
        """

        print((" " + "\n") * sellf.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))
