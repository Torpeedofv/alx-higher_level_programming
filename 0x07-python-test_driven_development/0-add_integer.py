#!/usr/bin/python3
"""A module for a function"""


def add_integer(a, b=98):
    """This is a function that adds to integers and returns the\
            sum of the integers"""

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")

    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
