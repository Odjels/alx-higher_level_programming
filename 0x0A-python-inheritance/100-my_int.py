#!/usr/bin/python3
'''my interger '''


class MyInt(int):
    '''myint class'''
    def __eq__(self, other):
        '''equality method'''
        if int.__eq__(self, other):
            return False
        return True

    def __ne__(self, other):
        '''not equal to method'''
        if int.__ne__(self, other):
            return False
        return True
