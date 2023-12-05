#!/usr/bin/python3

"""
Module: file_reader_module

This module provides a function for reading and printing the
content of a text file.
"""


def read_file(filename=""):
    """
    Read the content of a text file and print it to stdout.

    Parameters:
    - filename (str): The name of the text file to be read.
    Default is an empty string.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - UnicodeDecodeError: If there is an issue decoding the file as UTF-8.
    """
    with open(filename, encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end="")
