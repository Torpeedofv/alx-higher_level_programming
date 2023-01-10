#!/usr/bin/python3

"""A module for a function"""


def append_write(filename="", text=""):

    """A function that appends a string at the end of a text file"""

    with open(filename, 'a', encoding='utf-8') as filename:
        return filename.write(text)
