#!/usr/bin/python3
""" this module represents a class square """

class Square():
    """ initailizing data """
     def __init__(self, size=0):
         """square class with size attribute"""
        self.size = size

     @property
     def size(self):
          return self.__size
        """Get the size of the square."""


    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
         """ This sets the value of the attribute size."""

      def area(self):
              """ Returns the area of a square """
           return (self.__size ** 2)
