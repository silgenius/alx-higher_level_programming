#!/usr/bin/python3

"""
Module: file_writer_module

This module provides a function for writing a string to a text file
(UTF-8) and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write the provided string to a text file in UTF-8 encoding
    and return the number of characters written.

    Parameters:
    - filename (str): The name of the text file to which the
    string will be written. Default is an empty string.
    - text (str): The string to be written to the file.
    Default is an empty string.

    Returns:
    - int: The number of characters written to the file.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    """

    with open(filename, encoding="utf-8", mode="w") as f:
        return (f.write(text))
