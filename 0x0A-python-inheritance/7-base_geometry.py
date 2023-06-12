#!/usr/bin/python3
""" interger validator """


class BaseGeometry:
    """ tgis is an empty Geometry class """

    def __init__(self):
        """ Initialising data """
        pass

    def area(self):
        """ this calculates the area of a geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ this validates integer value """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
