#!/usr/bin/python3
""" Module to check the exact class type of an object """


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
