#!/usr/bin/python3

"""
Module: mylist_module

This module defines a custom class MyList
that inherits from the built-in list class.
"""


class MyList(list):
    """
    Class: MyList

    Represents a custom list class that inherits
    from the built-in list class.

    Methods:
    - print_sorted(self): Prints the elements of the
    list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """

        new_list = sorted(self)
        print(new_list)
