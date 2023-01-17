#!/usr/bin/python3
"""A class module"""

import json
class Base:
    """creation of an object Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
