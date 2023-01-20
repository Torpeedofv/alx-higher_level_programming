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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        if cls.__name__ == "Square": 
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        filename = f"{cls.__name__}.json"
        try:
            with open(filename) as f:
                list_of_dicts = cls.from_json_string(f.read())
        except (FileNotFoundError):
            return []
        instances_list = []
        for d in list_of_dicts:
            instances_list.append(cls.create(**d))
        return instances_list
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        
