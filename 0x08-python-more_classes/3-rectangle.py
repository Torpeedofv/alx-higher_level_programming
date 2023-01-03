#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represent a Rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initialize a new square"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an intefer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value

    def area(self):
        """calculates the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculates the area of the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)


