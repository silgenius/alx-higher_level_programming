#!/usr/bin/python3

"""
Module: inherits_from_module

This module provides a function for checking i
an object inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object inherits from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare the object against.

    Returns:
    - bool: True if the object inherits from the specified class,
    False otherwise.
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
