#!/usr/bin/python3
# 5-square.py
"""Defines a square"""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initializes a Square instance with an optional size"""

        self.size = size

    @property
    def size(self):
        """Retrieves the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns: The area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
