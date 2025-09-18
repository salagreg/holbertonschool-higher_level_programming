#!/usr/bin/python3
""" Module that defines a Square class with size and position. """


class Square:
    """
    Represents a square.

    Attributes:
    __size (int): Size of one side of the square.
    __position (tuple): Tuple of 2 non-negative integers to define position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
        size (int): The size of the square's side (default is 0).
        position: The position offset as a tuple of 2 non-negative integers.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Get the current position of the square.

        Returns:
            tuple: The current position (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 non-negative integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character considering position.
        If size is 0, it prints an empty line.
        The square is offset by spaces and newlines according to position.
        """
        if self.__size == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
