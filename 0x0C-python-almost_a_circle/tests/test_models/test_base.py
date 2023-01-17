#!/usr/bin/python3

import unittest
from models.base import Base

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

