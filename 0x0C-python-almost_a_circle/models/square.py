#!/usr/bin/python3
"""
Defines a module that contains class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes class Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        getter
        Retrieves size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets size to value
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns a string representation of the square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        assigns attributes
        *args is the list of arguments - no-keyworded arguments:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs - double pointer to a dictionary:
            key/value (keyworded arguments)
            must be skipped if *args exists and is not empty
        """
        if args:
            for a, b in enumerate(args):
                if a == 0:
                    self.id = b
                elif a == 1:
                    self.size = b
                elif a == 2:
                    self.x = b
                else:
                    self.y = b
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
