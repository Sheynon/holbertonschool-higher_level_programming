#!/usr/bin/python3
"""Defines a class Square with size and area"""


class Square:
    """Square class with private size attribute and area computation"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """return the size of the square"""
        return self.__size

    def area(self):
        """return the current square area"""
        return self.__size * self.__size
