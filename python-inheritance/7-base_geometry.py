#!/usr/bin/python3
""" This module defines a base class for geometry-related operations. """


class BaseGeometry:
    """
    This is a base class intended to be inherited by other geometry classes.
    It defines a method 'area()' that should be overridden in subclasses.
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
