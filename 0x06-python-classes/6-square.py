#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
         return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
         return self.__position

    @position.setter
    def position(self, value):
         if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(v, int) for v in value) and
                all(v >= 0 for v in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
         if self.__size == 0:
            print("")
        else:
            for c in range(self.__position[1]):
                print("")
            for a in range(self.__size):
                for n in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print('#', end="")
                print("")
