#!/usr/bin/python3
""" Module - 101-square
Defines a square based on 6-square """


class Square:
    """
    Defines a class Square
    Args: size - size of a square side
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes class Square
        Private instance attribute: size
            position
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        getter
        Retrieves position
        """
        return self.__position

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
        returns the current square area
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)

    def __str__(self):
        """
        String representation of square
        """
        string = ""
        if self.__size == 0:
            return string
        else:
            for i in range(self.__position[1]):
                string += '\n'
            for i in range(self.__size):
                string += " " * self.__position[0] + "#" * self.__size + '\n'
            return string[:-1]
