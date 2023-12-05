#!/usr/bin/python3

"""
Module: geometry

This module defines a base geometry class for calculating areas.
"""


class BaseGeometry:
    """
    Class: BaseGeometry

    Represents a base geometry class with an unimplemented
    area method.

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
