#!/usr/bin/python3
""" Module that defines a Square class. """


class Square:
    """ Class that defines a square by its size. """
    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): New size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: Area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' character.
        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
