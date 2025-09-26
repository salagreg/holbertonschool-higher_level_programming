#!/usr/bin/python3
"""
This module defines a base geometry class and
a rectangle class that inherits from it.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        int: The area computed as width multiplied by height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the Rectangle instance.

        The format follows: [Rectangle] <width>/<height>

        Returns:
        str: The formatted string describing the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


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
