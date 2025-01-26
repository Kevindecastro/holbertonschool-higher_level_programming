#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function `add_integer` ensures type checking and handles cases where the
inputs are floats by casting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casts floats to integers).

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
