#!/usr/bin/python3

"""creates a child class square"""

base = __import__('9-rectangle').Rectangle


class Square(base):

    """creation of a child class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()
