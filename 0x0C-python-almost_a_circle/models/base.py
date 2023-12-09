#!/usr/bin/python3

"""
Module: base_module

This module defines a Base class with an __init__ method
for managing object IDs.
"""


class Base:
    """
    Class: Base

    Represents a base class with an optional ID for object
    management.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an optional ID.

        Parameters:
        - id (int): An optional ID for the object.
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

