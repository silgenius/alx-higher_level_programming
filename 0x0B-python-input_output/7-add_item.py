#!/usr/bin/python3

"""
Module: add_item_module

This module provides a script for adding command-line
arguments to a Python list and saving them to a file in JSON format.
"""

from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_save_json():
    my_list = list(argv[1:])
    try:
        file_content = load_from_json_file("add_item.json")
    except FileNotFoundError:
        save_to_json_file(my_list, "add_item.json")
    else:
        file_content.extend(my_list)
        save_to_json_file(file_content, "add_item.json")


if __name__ == "__main__":
    add_save_json()
