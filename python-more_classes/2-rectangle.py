#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Rectangle class with private attribute width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return the area"""
        return self.__width * self.__height
    def perimeter(self):
        """Method to return the perimeter"""
        return (self.__width + self.__height) * 2
