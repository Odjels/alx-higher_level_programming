#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """ represents the rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """""getting the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """seting the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """seting the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
