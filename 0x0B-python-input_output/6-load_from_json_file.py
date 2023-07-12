#!/usr/bin/python3
"""Module defines a JSON file-reading function"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
