#!/usr/bin/python3
""" Module - 10-student
Defines a class Student that defines a student based on 9-student.py
"""


class Student:
    """
    Defines a student based on 9-student.py
    Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes a class student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for a in attrs:
                if a in self.__dict__.keys():
                    dic[a] = self.__dict__[a]
            return dic
