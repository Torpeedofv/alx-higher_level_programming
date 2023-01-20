#!/usr/bin/python3
"""A test module for a class"""


from models.square import Square
import unittest

class TestRectangle(unittest.TestCase):
    """A unittest class to test the Class rectangle"""

    def test_ids(self):
        """test ids"""
        s1 = Square(10)
        s2 = Square(4)
        s3 = Square(5, 6, 7, 8)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 8)
        s3.id = "b"
        self.assertEqual(s3.id, "b")

    def test_
