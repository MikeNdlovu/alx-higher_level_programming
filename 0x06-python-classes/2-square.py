#!/usr/bin/python3
""" class that validates the size of a square """


class Square:
    """ checks if size is positive and if it is a number

    Args:
        size: size of the square.

    Raises:
        TypeError: if size is not an int.
        ValueError: if size is less than 0.

    """
    def __init__(self, size=0):
        self._Square__size = size
        try:
            self._Square__size - 1
        except TypeError:
            raise TypeError('size must be an integer')
        if self._Square__size < 0:
            raise ValueError('size must be >= 0')
