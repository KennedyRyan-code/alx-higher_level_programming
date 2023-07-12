#!/usr/bin/python3
"""Writes a file-appending function."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) .

    Args:
        filename (str, optional): The name of the file
        If not provided, an empty string is assumed.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
