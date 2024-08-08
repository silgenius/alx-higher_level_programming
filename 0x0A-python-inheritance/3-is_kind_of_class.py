#!/usr/bin/python3

"""
Module: is_kind_of_class_module

This module provides a function for checking if an object is
an instance of a specified class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance of the
    specified class or its subclasses.

    Parameters:
    - obj: The object to be checked.
    - a_class: The class to compare the object against.

    Returns:
    - bool: True if the object is an instance of the
    specified class or its subclasses, False otherwise.
    """
    return (isinstance(obj, a_class))
