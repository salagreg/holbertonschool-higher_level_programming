#!/usr/bin/python3
"""
This module defines a function `lookup` that returns
the list of available attributes and methods of an object.
"""
def lookup(obj):
    """
    Return the list of available attributes and methods of an object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: List of attribute and method names of the object.
    """
    return dir(obj)
