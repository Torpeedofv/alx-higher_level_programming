#!/usr/bin/python3
"""Creates a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square.
        Args:
            size(int): the size of the new square.
            position(int, int): the position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get the current size of the square"""
        return size.__size

    @size.setter
    def size(self, value):
        """set the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position of the square"""
        if not isinstance(value, tuple) and
        len(value) != 2 and not isinstance(value[0], int) and not
        isinstance(value[1], int) and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the current area of the square"""
        return self.__size**2

    def my_print(self):
        """print the square with the # character"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
