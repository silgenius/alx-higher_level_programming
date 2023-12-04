#!/usr/bin/python3

"""
MagicClass Module

This module defines the MagicClass class, representing a simple abstraction
for a circle in mathematics. The class provides methods to calculate
the area and circumference of a circle based on its radius.

Classes:
- MagicClass: Represents a circle with methods for area and
circumference calculations.

Usage:
    To use this module, create an instance of MagicClass with
    a radius and then call the area() and circumference() methods.

"""

import math


class MagicClass:
    """
    A simple class representing a simple abstraction for a
    circle in mathematics.

    Attributes:
        - radius: The radius of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Parameters:
        - radius: A number (int or float) representing
        the radius of the circle.

        Raises:
        - TypeError: If the provided radius is not
        a number (neither int nor float).
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Formula: pi * radius^2

        Returns:
        - float: The calculated area of the circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Formula: 2 * pi * radius

        Returns:
        - float: The calculated circumference of the circle.
        """
        return (2 * math.pi * self.__radius)
