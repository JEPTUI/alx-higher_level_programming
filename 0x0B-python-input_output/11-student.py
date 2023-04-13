#!/usr/bin/python3
""" Module - 11-student
Defines a class Student that defines a student based on 10-student.py
"""


class Student:
    """
    defines a student based on 10-student
    Public instance attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes class Student
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

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of the Student instance
        """
        for i, j in json.items():
            setattr(self, i, j)
