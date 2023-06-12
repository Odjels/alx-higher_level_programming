#!/usr/bin/python3
'''module for only sub class'''


def inherits_from(obj, a_class):
    '''
    Return true if the object is an instance of a class
    '''
    return type(obj) != a_class and issubclass(type(obj), a_class)
