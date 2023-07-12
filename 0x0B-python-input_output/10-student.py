#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Class representing a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name,
        last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to be retrieved.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        obj_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    obj_dict[attr] = value
        return obj_dict
