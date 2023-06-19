#!/usr/bin/python3
'''
    Rectangle Class
'''
from models.base import Base


class Rectangle(Base):
    '''
        Rectangle class that Inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''
            getting private attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
            Setter forthe private attribute
        '''
        self.setter_validation("width", value)
        self.__width = value

    @property
    def height(self):
        '''
            getter for height private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting height private attribute
        '''
        self.setter_validation("height", value)
        self.__height = value

    @property
    def x(self):
        '''
            getting private attribute for x
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute for x
        '''
        self.setter_validation("x", value)
        self.__x = value

    @property
    def y(self):
        '''
            getting x private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting y private attribute
        '''
        self.setter_validation("y", value)
        self.__y = value

    def area(self):
        '''
            Returns the rectangle area
        '''
        return (self.height * self.width)

    def display(self):
        '''
            display the representation of the rectangle
        '''
        rectangle = ""
        print("\n" * self.y, end="")
        for a in range(self.height):
            rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        '''
            Updating the class arguments
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''
         a dictionary representation of this class
        '''
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}

    @staticmethod
    def setter_validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def __str__(self):
        '''
            the str method
        '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
