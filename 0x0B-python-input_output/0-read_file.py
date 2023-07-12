#!/usr/bin/python3
"""function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
