#!/bin/usr/python3
""" class that validates the size of a square """


class Square:
    """ checks if size is positive and if it is a number """
    def __init__(self, size=0):
        self._Square__size = size
        try:
            self._Square__size - 1
        except TypeError:
            raise TypeError('size must be an integer')
        if self._Square__size < 0:
            raise ValueError('size must be >= 0')
