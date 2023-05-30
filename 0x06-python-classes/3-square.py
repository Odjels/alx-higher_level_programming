#!/usr/bin/python3

class Square:
     def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
    """ 
    This is area of square
    Returns the area of the square
    """
