#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats together.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added.

    Returns:
        int: The sum of `a` and `b` as an integer.

    Raises:
        TypeError: If `a` or `b` is not an integer or float.

    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Return the addition of a and b
    return (a + b)
