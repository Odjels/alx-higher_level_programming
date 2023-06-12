#!/usr/bin/python3
""" module for base Geometry """


class BaseGeometry:
    """ this is an empty Geometry class """

    def __init__(self):
        """ Initialising data """
        pass

    def area(self):
        """ this calculates the area of a geometry """
        raise Exception("area() is not implemented")
