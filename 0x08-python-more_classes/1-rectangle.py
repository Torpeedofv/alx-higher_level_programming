#!/usr/bin/python3
"""Define a class, rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width of the current rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the size of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
