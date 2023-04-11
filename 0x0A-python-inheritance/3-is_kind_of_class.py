#!/usr/bin/python3
""" Module - 3-is_kind_of_class
Defines a function that checks if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is an instance of class
    that it inherited from
    """
    return isinstance(obj, a_class)
