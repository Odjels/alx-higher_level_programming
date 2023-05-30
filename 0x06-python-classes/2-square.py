#!/usr/bin/python3
""" this module represents a class square """

class Square:
    """ class creation with attribute size """
     def __init__(self, size=0):
         """ initializing data """
        if isinstance(size, int):
       """ checks the attribute if it is integer """
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
