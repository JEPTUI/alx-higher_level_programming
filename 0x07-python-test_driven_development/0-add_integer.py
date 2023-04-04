#!/usr/bin/python3
"""
Module - 0-add_integer
Takes two arguments of either int or float(casts to int) and returns sum int
"""


def add_integer(a, b=98):
    """
    Returns integer addition of a, b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # cast a and b to integers if they are float
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b
