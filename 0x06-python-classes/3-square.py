#!/usr/bin/python3
""" Module 3-square
Defines a square by based on 2-square """


class Square:
    """
    Defines a class Square
    Args: size - size of a square side
    """
    def __init__(self, size=0):
        """
        Initialization of class Square
        Private instance attribute: size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns current square area
        """
        area = (self.__size)**2
        return (area)
