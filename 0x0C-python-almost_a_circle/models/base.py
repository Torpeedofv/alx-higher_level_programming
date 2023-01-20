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
    
    @classmethod 
    def save_to_file(cls, list_objs):
        """a method that writes the JSON string representation to a file"""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            with open(filename, 'w') as f:
                f.write('[]')
        listsofdicts = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(listsofdicts)
        with open(filename, 'w') as f:
            f.write(json_str)
    
    def from_json_string(json_string):
        """Return the list of the JSON string"""

        if json_string is None:
            return []
        return json.loads(json_string)
