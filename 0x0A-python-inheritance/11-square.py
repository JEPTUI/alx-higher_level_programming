#!/usr/bin/python3
""" Module - 11-square
Defines class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a class Square
        Args: Private attributes:
            size(int)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Implements area method
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns [Square] <width>/<height>
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
