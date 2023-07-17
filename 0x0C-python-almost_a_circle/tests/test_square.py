#!/usr/bin/python3
"""Unittest for square.py file"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestSquare(unittest.TestCase):

    def test_square_initialization(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_square_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_display(self):
        expected_output = "#####\n" \
                          "#####\n" \
                          "#####\n" \
                          "#####\n"
        s = Square(5)
        self.assertEqual(s.display(), expected_output)

    def test_square_str(self):
        s = Square(5, 2, 1, 1)
        self.assertEqual(str(s), "[Square] (1) 2/1 - 5")

    def test_square_update(self):
        s = Square(5, 2, 1, 1)
        s.update(10, 7, 5, 2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 2)

    def test_square_update_kwargs(self):
        s = Square(5, 2, 1, 1)
        s.update(id=10, size=7, x=5, y=2)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 2)

    def test_square_to_dictionary(self):
        s = Square(5, 2, 1, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 1}
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
