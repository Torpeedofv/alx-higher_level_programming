#!/usr/bin/python3
"""A test Module"""


import sys
from io import StringIO
import unittest
from models.rectangle import Rectangle
from models.base import Base
 

class TestRectangle(unittest.TestCase):
    def test_ids(self):
        """test ids"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        
    def test_attributes(self):
        """Validates the attributes of the Rectangle"""

        Base._base__nb_objects = 0
        self.assertRaises(TypeError, Rectangle, 10, "2")
        self.assertRaises(ValueError, Rectangle, -10, 2)
        self.assertRaises(TypeError, Rectangle, 10, 2, {})
        self.assertRaises(ValueError, Rectangle, 10, 2, 3, -1)

    def test_area(self):
        """Validates the area of the Rectangle"""
        Base._base__nb_objects = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
       
    def test_display(self):
        """Validates the the print out in the stdout"""
        Base._base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(4, 2)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n")
        sys.stdout = mystdout = StringIO()
        r2 = Rectangle(2, 3, 2, 2)
        r2.display()
        self.assertEqual(mystdout.getvalue(), "\n\n  ##\n  ##\n  ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """Test strings"""
        Base._base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), f"[Rectangle] ({r2.id}) 1/0 - 5/5")

    def test_update(self):
        """Tests the Class update that assigns an argument to each attribute\
                """
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_dictionary(self):
        """tests dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {'x': 1, 'y': 9, 'width': 10, 'height': 2, 'id': 1})
        r1 = Rectangle(1, 1)
        r1_dictionary = r1.to_dictionary()
        self.assertDictEqual(r1_dictionary, {'x': 0, 'y': 0, 'width': 1, 'height': 1, 'id': 2})

    def test_RectCreate(self):
        """tests create"""
        Base._Base__nb_objects = 0
        s1 = Rectangle(10, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Rectangle.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)


    if __name__ == '__main__':
        unittest.main()
