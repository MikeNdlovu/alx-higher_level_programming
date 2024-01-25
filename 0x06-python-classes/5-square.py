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
        self.size = self._Square__size

    def size(self, value=0):
        """ sets new value of size """
        self.size = value

    def size(self):
        """ returns the value of size """
        return self.size

    def area(self):
        """ returns the area of the square """
        try:
            return self.size * self.size
        except TypeError:
            raise TypeError('size must be an integer')

    def my_print(self):
        """ prints a square """
        lines = 0
        if self.size == 0:
            print()
        else:
            while lines < self.size:
                print("#" * self.size)
                lines += 1
