#!/usr/bin/python3

"""
Module: geometry

This module defines a base geometry class for calculating areas.
"""


class BaseGeometry:
    """
    Class: BaseGeometry

    Represents a base geometry class with an unimplemented area method.

    Methods:
    - area(self): Raises an exception indicating tha
    the area method is not implemented.
    """

    def area(self):
        """
        Raises an exception indicating that the area method
        is not implemented.

        Raises:
        - Exception: Always raises an exception with the
        message "area() is not implemented".
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if the provided value is an integer.

        Parameters:
            - name (str): The name or identifier of the value being validated.
            - value: The value to be validated.

        Raises:
            - TypeError: If the provided value is not an integer.
            - ValueError: if value provided is less than 0.
        """

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
