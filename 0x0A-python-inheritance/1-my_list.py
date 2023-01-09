#!/usr/bin/python3

"""Module for MyList"""


class MyList(list):
    """prints sorted list of class"""
    def print_sorted(self):
        print(sorted(self))
