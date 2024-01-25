#!/bin/usr/python3
""" class that validates the size of a square """


class Square:
    """ checks if size is positive and if it is a number """
    def __init__(self, size=0):
        self._Square__size = size
        try:
            """ validatesif size is a number """
            self._Square__size - 1
        except TypeError:
            """ if not it raises a typeError """
            raise TypeError('size must be an integer')
        if self._Square__size < 0:
            """ validates if size is a positive number """
            raise ValueError('size must be >= 0')
