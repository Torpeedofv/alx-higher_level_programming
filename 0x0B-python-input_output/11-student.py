#!/usr/bin/python3

"""A class module"""


class Student:

    """creation of a class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {key: value for key, value in self.__dict__.items()}
        else:
            return {key: value for key, value in self.__dict__.item() if key in self}
        def reload_from_json(self, json):
            for key, value in json.items():
                setattr(self, key, value)
