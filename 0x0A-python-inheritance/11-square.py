#!/usr/bin/python3
'''square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''initializing the square object'''
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        '''area of the square'''
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
