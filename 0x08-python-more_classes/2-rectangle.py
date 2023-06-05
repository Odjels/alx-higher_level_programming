#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
