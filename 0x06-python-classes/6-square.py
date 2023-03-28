#!/usr/bin/python3
""" Module 6-square
Defines a square by based on 5-square """


class Square:
    """
    Defines a class Square
    Args: size - size of a square side
    Functions:
        size(self)
        size(self, value)
        position(self)
        position(self, value)
        __init__()
        area(self)
        my_print(self)
     """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes class Square
        Attributes: size
                    position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getter
        Retrieves size
        """
        return size.__size

    @size.setter
    def size(self, value):
        """
        sets size to value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter
        Retrieves position
        """
        return size.__position

    @position.setter
    def position(self, value):
        """
        Sets position to value
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Returns the current square area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
