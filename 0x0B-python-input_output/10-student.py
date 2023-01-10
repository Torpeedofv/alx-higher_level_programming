#!/usr/bin/python3

"""A class Module"""


class Student:

    """creation of the student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
