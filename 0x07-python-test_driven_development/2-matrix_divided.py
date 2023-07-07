#!/usr/bin/python3
"""Divides all elements of a matrix by a given number."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists: The new matrix with elements divided by `div`.

    Raises:
        TypeError: If `matrix` is not a matrix (list of lists) of integers,
                   float or if `div` is not a number (integer or float).
        ZeroDivisionError: If `div` is equal to 0.
        TypeError: If each row of the matrix does not have the same size.

    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round to 2 decimal places
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return (new_matrix)
