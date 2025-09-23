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
