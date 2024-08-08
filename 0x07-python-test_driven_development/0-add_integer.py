#!/usr/bin/python3

"""
A simple module that performs addition
"""

def add_integer(a, b=98):
    """
    Adds two numbers and returns their sum.

    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float, optional): The second number to be added.
    Defaults to 98.

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If either 'a' or 'b' is not an integer or float.
    """
    # Check if a and b are integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b

