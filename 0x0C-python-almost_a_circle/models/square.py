#!/usr/bin/python3
"""importing Rectangle Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing data"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """settir for Square size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """ updating the square class"""
        if len(args):
            for b, arg in enumerate(args):
                if b == 0:
                    self.id = arg
                elif b == 1:
                    self.size = arg
                elif b == 2:
                    self.x = arg
                elif b == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returning dictonary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
