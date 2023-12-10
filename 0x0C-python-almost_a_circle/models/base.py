#!/usr/bin/python3

"""
Module: base_module

This module defines a Base class with an __init__ method
for managing object IDs.
"""

import json


class Base:
    """
    Class: Base

    Represents a base class with an optional ID for object
    management.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an optional ID.

        Parameters:
        - id (int): An optional ID for the object.
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        a list of dictionaries.

        Parameters:
        - list_dictionaries (list): A list of dictionaries.

        Returns:
        - str: The JSON string representation of list_dictionaries.
        If list_dictionaries is None or empty, returns "[]".
        """

        if list_dictionaries and list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))
