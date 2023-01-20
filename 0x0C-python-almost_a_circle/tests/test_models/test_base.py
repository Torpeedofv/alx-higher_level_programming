#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os

class TestBase(unittest.TestCase):
    def test_id(self):
        Base.Base__nb_objects = 0
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        base4 = Base()
        base5 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 3)
        self.assertEqual(base5.id, 4)

class TestToJsonString(unittest.TestCase):
    def test_valid_input(self):
        print('test_valid_input')
        list_dictionaries = [{'x': 1, 'y': 2}, {'a': 3, 'b': 4}]
        expected_output = json.dumps(list_dictionaries)
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)

    def test_empty_input(self):
        print('test_empty_input')
        list_dictionaries = []
        expected_output = '[]'
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)

    def test_none_input(self):
        print('test_None_input')
        list_dictionaries = None
        expected_output = '[]'
        self.assertEqual(Base.to_json_string(
            list_dictionaries), expected_output)


class TestFromJsonString(unittest.TestCase):
    def test_valid_input(self):
        print('test_valid_input')
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_string = json.dumps(list_input)
        expected_output = [{'height': 4, 'width': 10, 'id': 89}, {
            'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_empty_input(self):
        print('test_empty_input')
        json_input = ''
        expected_output = []
        self.assertEqual(Base.from_json_string(json_input), expected_output)

    def test_none_input(self):
        print('test_none_input')
        json_input = None
        expected_output = []
        self.assertEqual(Base.from_json_string(json_input), expected_output)
        """ with self.assertRaises(TypeError):
            Base.from_json_string(json_input) """
