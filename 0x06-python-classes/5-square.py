#!/usr/bin/python3
""" this module represents a class square """

class Square():
    """Represents a square class """
    def __init__(self, size=0):
        """Initialize data"""
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
          """ Returns the area of a square """
          return (self.__size ** 2)

    def my_print(self):
          """ print square of using hashes """
          if self.__size == 0:
            print("")
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print('#', end="")
                print("")
                """prints the square with character # """
