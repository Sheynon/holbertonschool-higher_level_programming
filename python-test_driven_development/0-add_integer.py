#!/usr/bin/python3
"""
Module that defines the add_integer function to add two integers.
"""
def add_integer(a, b=89):
    """
    Adds two integers or floats, casting floats to ints

    Args:
        a: The First Number (int or float).
        b: The Second Number (int or float, default is 98).

    Returns:
        The sum of a and b as an interger.

    Raises:
        TypeErrir: If a or b are not intergers or flats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = a + b
    return result
