#!/usr/bin/python3

"""
Module: json_file_writer_module

This module provides a function for writing an object to
a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the provided object to a text file using its JSON representation.

    Parameters:
    - my_obj: The object to be saved to the file.
    - filename (str): The name of the text file to
    which the object will be written.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        json_file = json.dumps(my_obj)
        f.write(json_file)
