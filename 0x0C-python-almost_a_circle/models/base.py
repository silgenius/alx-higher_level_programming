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
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representatio
        of list_objs to a file.

        Parameters:
        - cls (type): The class itself.
        - list_objs (list): A list of instances that inherit from Base.

        Note: If list_objs is None, an empty list is saved.
              The filename is constructed as "<Class name>.json",
              for example, "Rectangle.json".
              Uses the static method to_json_string for JSON serialization.
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of dictionaries
        represented by a JSON string.

        Parameters:
        - json_string (str): A string representing a list of
        dictionaries in JSON format.

        Returns:
        - list: The list of dictionaries represented by json_string.
        If json_string is None or empty, returns an empty list.
        """

        if json_string and json_string is not None:
            return json.loads(json_string)
        return []
