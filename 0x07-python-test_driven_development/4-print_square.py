#!/usr/bin/python3
""" Module - 4-print_square
Defines a function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with character #
    Args: size-size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
