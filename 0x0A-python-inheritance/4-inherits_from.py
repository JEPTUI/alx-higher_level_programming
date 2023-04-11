#!/usr/bin/python3
""" Module - 4-inherits_from
Defines a function that checks if the object is an instance of a
class that inherited from the specified class otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is instance of class that it
    inherits from or is subclass of otherwise False
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
