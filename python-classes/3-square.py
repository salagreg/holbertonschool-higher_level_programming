#!/usr/bin/python3
""" This module allows you to create a square and compute its area. """


class Square:
    """ Represents a square. """
    def __init__(self, size=0):
        """
        Initializes a square.

        Args:
            size (int): The size of one side of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Computes and returns the area of the square. """
        return self.__size ** 2
