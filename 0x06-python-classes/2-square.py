#!/usr/bin/python3
"""Module 2-square
Defines a square by based on 1-square"""


class Square:
    """
    Definition for class Square
    Args: size(int) - size of a square side
    """

    def __init__(self, size=0):
        """
        Initialization of class Square

        Private instance attribute: size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size
