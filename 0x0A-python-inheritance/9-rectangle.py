#!/usr/bin/python3
""" Module - 9-rectangle
Defines a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes class Rectangle
        Args: Private attributes
            width(int)
            height(int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Implements area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns [Rectangle] <width>/<height>
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
