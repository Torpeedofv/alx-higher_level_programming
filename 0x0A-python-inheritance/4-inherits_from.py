#!/usr/bin/python3

"""A module for a function"""


def inherits_from(obj, a_class):

    """A function that checks if an object is an instance of a class or super
    class"""

    return type(obj) != a_class and issubclass(type(obj), a_class)
