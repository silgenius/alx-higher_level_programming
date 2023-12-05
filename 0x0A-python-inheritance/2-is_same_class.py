#!/usr/bin/python3

"""
Module: is_same_class_module

This module provides a function for checking if an
object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare the object against.

    Returns:
    - bool: True if the object is an instance of the
    specified class, False otherwise.
    """

    return a_class == type(obj)
