#!/usr/bin/python3

"""
Module: json_file_loader_module

This module provides a function for creating an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file from which the
    object will be loaded.

    Returns:
    - object: The Python object created from the JSON file.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - json.JSONDecodeError: If there is an issue decoding the JSON file.
    """

    with open(filename, encoding="utf-8") as f:
        file_content = f.read()
        file_content = json.loads(file_content)

        return file_content
