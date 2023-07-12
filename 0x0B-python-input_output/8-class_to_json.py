#!/usr/bin/python3
"""Module Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure for JSON.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary description of the object for JSON serialization.
    """
    obj_dict = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            obj_dict[attr] = value
    return obj_dict
