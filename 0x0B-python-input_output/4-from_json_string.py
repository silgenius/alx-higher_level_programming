#!/usr/bin/python3

"""
Module: json_parser_module

This module provides a function for parsing a JSON string
and returning the corresponding Python data structure.
"""

import json


def from_json_string(my_str):
    """
    Parse the provided JSON string and return the corresponding
    Python data structure.

    Parameters:
    - my_str (str): The JSON string to be parsed.

    Returns:
    - object: The Python data structure represented by the JSON string.
    """

    return (json.loads(my_str))
