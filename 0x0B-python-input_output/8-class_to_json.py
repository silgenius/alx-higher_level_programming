#!/usr/bin/python3

"""
Module: json_serializer_module

This module provides a function for converting an object to a
dictionary description suitable for JSON serialization.
"""


def class_to_json(obj):
    """
    Convert the provided object to a dictionary description
    with a simple data structure (list, dictionary, string,
    integer, and boolean) for JSON serialization.

    Parameters:
    - obj: An instance of a Class. All attributes of the
    obj Class must be serializable.

    Returns:
    - dict: A dictionary description representing the
    serializable attributes of the object.
    """

    if isinstance(obj, (str, int, bool)):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        obj_dict = vars(obj)
        return {key: class_to_json(value) for key, value in obj_dict.items()}
    else:
        raise TypeError
