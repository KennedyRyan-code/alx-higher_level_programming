#!/usr/bin/python3
"""Unittest for base.py file"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_initialization(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_base_custom_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])
        self.assertEqual(json_string, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_from_json_string(self):
        list_dicts = Base.from_json_string(None)
        self.assertEqual(list_dicts, [])

        list_dicts = Base.from_json_string("")
        self.assertEqual(list_dicts, [])

        list_dicts = Base.from_json_string('[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')
        self.assertEqual(list_dicts, [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])

    def test_save_to_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])

        with open("Base.json", "r") as file:
            json_data = file.read()
            self.assertEqual(json_data, '[{"id": 1}, {"id": 2}]')

    def test_load_from_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Base)
        self.assertIsInstance(instances[1], Base)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].id, 2)

    def test_create_instance(self):
        dictionary = {'id': 1, 'name': 'John', 'age': 25}
        instance = Base.create(**dictionary)
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 25)

    def test_create_instance_without_id(self):
        dictionary = {'name': 'John', 'age': 25}
        instance = Base.create(**dictionary)
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 25)


if __name__ == '__main__':
    unittest.main()
