#!/usr/bin/python3
""" Module - 3-say_my_name
Defines a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Args: first_name(string)
        last_name(string)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
