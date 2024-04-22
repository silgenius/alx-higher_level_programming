#!/usr/bin/python3

"""
Module: base_module

This module defines a Base class with an __init__ method
for managing object IDs.
"""

import csv
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

        if (list_dictionaries) or (list_dictionaries is not None):
            return json.dumps(list_dictionaries)
        bracket = []
        return json.dumps(bracket)

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
            f.write(
                    cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])
                    )

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

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes already set.

        Parameters:
        - cls (type): The class itself.
        - **dictionary (dict): A dictionary containing attribute values.

        Returns:
        - instance: An instance of the class with attributes set
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                file_content = f.read()
                instance_list = []
                for item in cls.from_json_string(file_content):
                    item = cls.create(**item)
                    instance_list.append(item)
            return instance_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method to serialize instances to a CSV file.

        Parameters:
        - list_objs (list): A list of instances to be serialized.

        The method writes the serialized data to a CSV file named
        <Class name>.csv using the csv.DictWriter class.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fieldnames = ['id', 'size', 'x', 'y']
            else:
                raise ValueError(f"Unsupported class: {cls.__name__}")

            data = [obj.to_dictionary() for obj in list_objs]
            csv_writer = csv.DictWriter(f, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method to deserialize instances from a CSV file.

        Returns:
        - list: A list of instances deserialized from the CSV file.

        The method reads a CSV file named <Class name>.csv and
        creates instances
        of the class using the create() method with the data from the file.
        If the file is not found, an empty list is returned.
        """

        rectangles = []
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    for key in row.keys():
                        row[key] = int(row[key])
                    rectangle = cls.create(**row)
                    rectangles.append(rectangle)
            return rectangles
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        # Function to draw a rectangle
        def draw_rectangle(rectangle):
            turtle.penup()
            turtle.goto(rectangle.width / 2, rectangle.height / 2)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(rectangle.width)
                turtle.right(90)

        # Function to draw a square
        def draw_square(square):
            turtle.penup()
            turtle.goto(square.width / 2, square.height / 2)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.width)
                turtle.right(90)

        # Draw rectangles
        turtle.color("blue")
        for rectangle in list_rectangles:
            draw_rectangle(rectangle)

        # Draw squares
        turtle.color("red")
        for square in list_squares:
            draw_square(square)

        turtle.done()
