#!/usr/bin/python3
"""
Defines a class Rectangle that inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits from Base
    Private instance attributes:
        __width
        __height
        __x
        __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter
        Retrieves width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets width to value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter
        Retrieves height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets height to value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        getter
        Retrieves x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets x to value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        getter
        Retrieves y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets y to value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        method that returns the string representation of rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Updates class Rectangle by adding public method that assigns an
        argument to each attribute:
        *args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute

        **kwags: assigns a key/value argument to attributes
        """
        if args:
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                elif a == 1:
                    self.width = b
                elif a == 2:
                    self.height = b
                elif a == 3:
                    self.x = b
                else:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Returns dictionary representation of the rectangle
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
