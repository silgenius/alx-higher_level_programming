#!/usr/bin/python3

"""
Module: file_appender_module

This module provides a function for inserting a line of text
into a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text into a file after each line containing a specific string.

    Parameters:
    - filename (str): The name of the file to be modified.
    - search_string (str): The specific string to search for in each line.
    - new_string (str): The line of text to be inserted after each line containing the search string.
    """
    
    with open(filename"", encoding="utf-8") as f:
        
        while line = f.read_line():
            word = ""
            for i in line:
                word += i
                if new_string == word:
                    x += 1
                if i == " " or i == '\n':
                    word = ""
            f.write

