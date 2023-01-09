#!/usr/bin/python3

""" A module that for a child class Square"""


base = __import__('9-rectangle').Rectangle


class Square(base):

    """creates a child class Square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
