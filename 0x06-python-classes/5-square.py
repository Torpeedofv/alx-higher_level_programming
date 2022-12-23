#!/usr/bin/python3
"""Define a class, Square."""


class Square:
    """represent a square."""

    def __init__(self, size=0):
        """initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get the size of the current square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Calculate the current area of the square."""
        return (self.__size)**2

    def my_print(self):
        """Prints the character # in the stdout."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
            if self.__size == 0:
                print()
