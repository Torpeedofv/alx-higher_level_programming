#!/usr/bin/python3

"""A module to read a file"""


def read_file(filename=""):

    """a function to read a file"""

    with open(filename, encoding="utf-8") as filename:
        print(filename.read(), end="")
