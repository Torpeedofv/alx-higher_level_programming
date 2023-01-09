#!/usr/bin/python3
base = __import__('7-base_geometry').BaseGeometry
"""A module for a child class Rectangle"""


class Rectangle(base):

    """creation of a class Rectangle"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
