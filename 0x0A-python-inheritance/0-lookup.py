#!/usr/bin/python3

"""
Module: lookup_module

This module provides a function for looking up
and printing the list of attributes and methods of an object.
"""


def lookup(obj):
    """
    Prints the list of attributes and methods of the given object.

    Parameters:
    - obj: The object for which the attributes and
    methods are to be looked up.
    """

    return dir(obj)
