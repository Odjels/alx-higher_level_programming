#!/usr/bin/python3
"""
   Student to json with filter
"""


class Student:
    """
         class students that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializing the Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
            getting a dictionary representation for the Student.
        """

        if attr is not None:
            result = {a: self.__dict__[a] for a in self.__dict__.keys() & attr}
            return result
        else:
            return self.__dict__
