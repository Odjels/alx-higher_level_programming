#!/usr/bin/python3

class Square():
     def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
         return (self.__size)

    @size.setter
    def size(self, value):
         if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, other):
         return self.__size == other.__size

    def __ne__(self, other):
         return self.__size != other.__size

    def __gt__(self, other):
         return self.__size > other.__size

    def __ge__(self, other):
         return self.__size >= other.__size

    def __lt__(self, other):
          return self.__size < other.__size

    def __le__(self, other):
         return self.__size <= other.__size
