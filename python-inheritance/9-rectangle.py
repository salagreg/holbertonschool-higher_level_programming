#!/usr/bin/python3
"""
This module defines a base geometry class and
a rectangle class that inherits from it.
"""


class BaseGeometry:
    """
    BaseGeometry is a base class for other geometry classes.
    """
    def area(self):
        """
        Compute the area of the geometry shape.

        Raises:
            Exception: Always raises an exception to indicate that the
            method is not implemented in the base class.

        This method is meant to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.

        Args:
        name (str): The name of the parameter to validate.
        value (int): The value to validate.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
