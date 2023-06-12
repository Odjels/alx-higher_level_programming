#!/usr/bin/python3
""" parent class list and its sub class"""


class MyList(list):
    """ childclass inherites from list class """

    def print_sorted(self):
        """ print the sorted copy of list """
        recent_list = list.copy(self)
        list.sort(recent_list)
        print(recent_list)
