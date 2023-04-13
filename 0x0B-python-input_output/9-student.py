#!/usr/bin/python3
""" Module - 9-student
Defines a class Student that defines a student
"""


class Student:
    """
    defines a student
    Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        return self.__dict__
