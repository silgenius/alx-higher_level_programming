#!/usr/bin/python3

"""
Module: student_module

This module defines a Student class with public instance attributes and
a method for retrieving a dictionary representation.
"""


class Student:
    """
    Class: Student

    Represents a student with attributes first_name, last_name, and age.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - __init__(self, first_name, last_name, age):
    Initializes a new student instance.
    - to_json(self): Retrieves a dictionary representation of
    a Student instance.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student instance.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
        - dict: A dictionary representing the student instance.
        """
        return self.__dict__
