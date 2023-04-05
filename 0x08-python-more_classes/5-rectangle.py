#!/usr/bin/python3
""" Module - 5-rectangle
Defines a rectangle based on 4-rectangle.py """


class Rectangle:
    """
    Defines a class Rectangle
    Private instance attribute:
            width(int)
            height(int)
    """

    def __init__(self, width=0, height=0):
        """
        Initializes class rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter
        Retrieves the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets width to value
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
        Retrieves the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets height to value
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
            return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """
        Print the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for rows in range(self.__height)])

    def __repr__(self):
        """
        Returns string representation of the
        rectangle to recreate a new instance
        """
        return "Rectangle({}, {}".format(self.width, self.height)

    def __del__(self):
        """
        Deletes an instance of Rectangle
        """
        print("Bye rectangle...")
