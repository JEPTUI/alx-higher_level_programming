#!/usr/bin/python3
""" Module - 1-write_file
Defines a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns
    number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        chars = f.write(text)
    return chars
