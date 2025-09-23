#!/usr/bin/python3
"""
This module provides a function to determine if an object
is an instance of a subclass (strictly) of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare inheritance against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class
              (but not if it is an instance of a_class itself),
              False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
