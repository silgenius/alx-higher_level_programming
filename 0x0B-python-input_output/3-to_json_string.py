#!/usr/bin/python3

"""
Module: json_converter_module

This module provides a function for converting an object
to its JSON representation as a string.
"""

import json


def to_json_string(my_obj):
    """
    Convert the provided object to its JSON representation as a string.

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
