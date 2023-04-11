#!/usr/bin/python3
""" Module - 2-is_same_class
Defines a function that checks if
object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance of the specified class
    otherwise False
    """
    return type(obj) == a_class
