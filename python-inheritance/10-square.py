#!/usr/bin/python3
"""
This module defines a base geometry class and
a rectangle class that inherits from it.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle """
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size (length of a side) of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
