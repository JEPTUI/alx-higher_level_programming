#!/usr/bin/python3
""" Module - 9-rectangle
Defines a rectangle based on 8-rectangle.py """


class Rectangle:
    """
    Defines a class rectangle
    private instance attribute:
            width(int)
            height(int)
    class attribute:
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
        Retrieves height
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
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """
        Print the rectangle with the character #
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rext_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance
        """
        return cls(size, size)
