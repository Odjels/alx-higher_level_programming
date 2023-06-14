#!/usr/bin/python3
'''Student to disk and board.'''


class Student:
    '''Class for jsonification.'''
    def __init__(self, first_name, last_name, age):
        '''initializiation.'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''getting dictionary with filter.'''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {b: c for b, c in self.__dict__.items() if b in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Loading the attributes from json.'''
        for key, value in json.items():
            self.__dict__[key] = value
