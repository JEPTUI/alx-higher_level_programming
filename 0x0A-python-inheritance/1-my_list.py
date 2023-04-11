#!/usr/bin/python3
""" Module - 1-my_list
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    Inherits from list
    Public instance method: def print_sorted(self)
    """
    def print_sorted(self):
        """
        Prints the sorted list in ascending order
        """
        print(sorted(self))
