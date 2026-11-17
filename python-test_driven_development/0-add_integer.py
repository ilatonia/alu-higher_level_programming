#!/usr/bin/python3
"""Module for add_integer.

Provides a function that adds two integers.
Floats are casted to integers before the addition.
"""


def add_integer(a, b=98):
    """Add two integers.
    Return the addition of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
