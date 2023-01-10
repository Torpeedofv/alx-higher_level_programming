#!/usr/bin/python3

"""A module for a function"""


import json


def save_to_json_file(my_obj, filename):

    """A function that writes an object to a text file\
            using a Json Representation"""

    with open(filename, 'w') as filename:
        return json.dump(my_obj, filename)
