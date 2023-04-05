#!/usr/bin/python3
"""Module - 7-rectangle
Defines a rectangle based on based on 6-rectangle.py """


class Rectangle:
    """
    Defines a clas rectangle
    Private instance attribute:
            width(int)
            height(int)
    class attributes:
        number_of_instances
        print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a class rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Deletes an instance of a class
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @property
    def width(self):
        """
        Getter
        Retrieves width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width to value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter
        Retrieves height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height to value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self._width) + (2 * self.__height)

    def __str__(self):
        """
        Print the rectangle with the character(s) stored in print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width
                         for rows in range(self.__height)])

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
