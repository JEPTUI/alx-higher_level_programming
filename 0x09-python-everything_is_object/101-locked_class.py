#!/usr/bin/python3
""" Module - 101-locked_class
Defines a class with no class or object attribute """


class LockedClass:
    """
    Defines a class that prevents user from creating
    new instance attributes if the new instance attribute is called first_name
    """
    __slots__ = "first_name"
