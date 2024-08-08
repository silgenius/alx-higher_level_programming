#!/usr/bin/python3

"""
Module: add_attribute_module

This module provides a function for adding a new
attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to the given object.

    This function checks if the object has a '__dict__' attribute
    (indicating it can have attributes),
    and then adds the specified attribute with the provided value.

    Parameters:
    - obj: The object to which the attribute will be added.
    - attr: The name of the attribute to be added.
    - value: The value of the new attribute.
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
