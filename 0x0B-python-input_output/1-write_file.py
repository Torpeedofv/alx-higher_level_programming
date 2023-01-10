#!/usr/bin/python3

"""A module for a function"""


def write_file(filename="", text=""):

    """a function that writes a string to a text file"""

    with open(filename, 'w', encoding="utf-8") as filename:
        return filename.write(text)
