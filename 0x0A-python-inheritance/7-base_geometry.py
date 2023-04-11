#!/usr/bin/python3
""" Module - 7-base_geometry
Defines a class BaseGeometry based on 6-base_geometry.py
"""


class BaseGeometry:
    """
    Public instance methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        raises an Exception with the message not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value(int)
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
