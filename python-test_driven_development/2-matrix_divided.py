#!/usr/bin/python3
"""Module for matrix_divided.

Provides a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Args:
        matrix: a list of lists of integers or floats.
        div: the number (integer or float) to divide by.

    Returns:
        A new matrix with every element divided by div and rounded to
        2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats,
            if the rows do not all have the same size, or if div is not
            a number.
        ZeroDivisionError: if div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
