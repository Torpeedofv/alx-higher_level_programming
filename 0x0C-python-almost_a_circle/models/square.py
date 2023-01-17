#!/usr/bin/python3
"""A class module"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Creation of a an Object Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """returns the size"""
        return self.width or self.height

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class by adding public method that assigns attributes\
                """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

