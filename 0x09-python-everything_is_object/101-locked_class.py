#!/usr/bin/python3

"""
Module: locked_class_module

Provides a simple class with a locked attribute.

Classes:
    - LockedClass: A class with a locked attribute
    'first_name' using __slots__.
"""


class LockedClass:
    """
    A class with a locked attribute 'first_name' using __slots__.

    Attributes:
        - first_name (str): The first name of an instance.

    Methods:
        -__init__(self, first_name=""): Initializes a
        new instance of LockedClass.

    Default value for 'first_name' is an empty string.
    """
    __slots__ = ("first_name")

    def __init__(self, first_name=""):
        """
        Initializes a new instance of LockedClass.

        Parameters:
        - first_name (str, optional): The first name for
        the instance. Defaults to an empty string.
        """

        self.first_name = first_name
