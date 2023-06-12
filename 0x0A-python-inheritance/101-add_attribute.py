#!/usr/bin/python3
'''Attribute'''


def add_attribute(object, name, value):
    '''this function adds new attribute to the obj'''
    if '__dict__' in dir(object):
        object.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
