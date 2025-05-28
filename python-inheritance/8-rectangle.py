#!/usr/bin/python3
"""Defines BaseGeometry Class"""


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
