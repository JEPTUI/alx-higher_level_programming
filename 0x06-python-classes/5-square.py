#!/usr/bin/python3
""" Module 5-square
Defines a square by based on 4-square """


class Square:
    """
    Defines a class Square
    Args: size - size of square side
    Functions:
        size(self)
        size(self, value)
        __init__()
        area(self)
        my_print(self)
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
        Getter
        Retrieves size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size to vale
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns  the current square area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
