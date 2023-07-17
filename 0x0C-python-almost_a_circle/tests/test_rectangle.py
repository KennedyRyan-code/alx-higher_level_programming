#!/usr/bin/python3
"""Unittest for rectangle.py file"""
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_rectangle_initialization(self):
        r = Rectangle(10, 5, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_rectangle_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_rectangle_display(self):
        expected_output = "##########\n" \
                          "##########\n" \
                          "##########\n"
        r = Rectangle(10, 3)
        self.assertEqual(r.display(), expected_output)

    def test_rectangle_str(self):
        r = Rectangle(5, 3, 2, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/1 - 5/3")

    def test_rectangle_update(self):
        r = Rectangle(5, 3, 2, 1, 1)
        r.update(10, 7, 4, 5, 2)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 2)

    def test_rectangle_update_kwargs(self):
        r = Rectangle(5, 3, 2, 1, 1)
        r.update(id=10, width=7, height=4, x=5, y=2)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 2)

    def test_rectangle_to_dictionary(self):
        r = Rectangle(5, 3, 2, 1, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 3, 'x': 2, 'y': 1}
        self.assertDictEqual(r.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
