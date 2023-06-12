#!/usr/bin/python3
""" module for same class checking """


def is_same_class(obj, a_class):
    """ returns true if the object is an instance of a class """
    return type(obj) is a_class
