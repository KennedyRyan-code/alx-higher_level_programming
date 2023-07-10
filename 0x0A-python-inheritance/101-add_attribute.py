#!/usr/bin/python3
"""Defines a function that adds attributes to objects"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
