#!/usr/bin/python3
""" Module - 102-square
Defines a square based on 4-square """


class Square:
    """
    Defines a class Square
    Args: size - size of a square side
    """

    def __init__(self, size=0):
        """
        Initializes a class Square
        Private instance attribute: size
        """
        self.size = size

    @property
    def size(self):
        """"
        Getter
        Retrieves size
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
        returns the current square area
        """
        return (self.__size)**2

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.size != other.size

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        return self.size >= other.size
