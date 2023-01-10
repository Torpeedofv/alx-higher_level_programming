#!/usr/bin/python3

"""A module for a function"""


import json


def load_from_json_file(filename):

    """A function that creates an object from a JSON file"""

    with open(filename, 'r') as filename:
        return json.load(filename)
