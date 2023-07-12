#!/usr/bin/python3
"""Module defines a class Student"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance with the given name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        obj_dict = {}
        for attr in self.__dict__:
            value = getattr(self, attr)
            if isinstance(value, (list, dict, str, int, bool)):
                obj_dict[attr] = value
        return obj_dict
