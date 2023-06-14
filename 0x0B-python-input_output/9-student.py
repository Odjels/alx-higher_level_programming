#!/usr/bin/python3
"""student to json"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returning the  __dict__ attribute"""
        return vars(self)
