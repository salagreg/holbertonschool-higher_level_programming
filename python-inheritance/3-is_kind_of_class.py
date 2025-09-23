#!/usr/bin/python3
"""
Module to check if an object is an instance of a class or
a class that inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of the specified class or a subclass.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
    True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
