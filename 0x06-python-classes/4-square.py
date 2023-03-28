#!/usr/bin/python3
""" Module 4-square
Defines square by based on 3-square """


class Square:
    """
    Defines a class square
    Args: size(int) - size of a square side
    Functions:
        __init__()
        area(self)
    """
    def __init__(self, size=0):
        """
        Initializes class Square
        Private instance attribute: size
        """
        self.__size = size

    @property
    def size(self):
        """
        getter
        Retrieve size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size to value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the current square area
        """
        return (self.__size)**2
