#!/usr/bin/python3
"""Write a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """
        Inverted equality comparison.

        Args:
            other: The object to compare against.

        Returns:
            True if the values are not equal; False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality comparison.

        Args:
            other: The object to compare against.

        Returns:
            True if the values are equal; False otherwise.
        """
        return super().__eq__(other)
