#!/usr/bin/python3
""" Module - 100-my_int
Defines class MyInt that inherits from int
"""


class MyInt(int):
    """
    Inherits from int
    MyInt has == and != operators inverted
    """
    def __init__(self,size):
        """
        Initializes class
        """
        self.size = size

    def __eq__(self, value):
        """
        Invert == operator to !=
        """
        return self.size != value

    def __ne__(self, value):
        """
        Invert != to ==
        """
        return self.size == value
