#!/usr/bin/python3

"""A module for a function"""


import json


def from_json_string(my_str):

    """A function that returns an object represented by\
            a JSON string"""

    return json.loads(my_str)
