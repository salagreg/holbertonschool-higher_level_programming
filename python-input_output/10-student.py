#!/usr/bin/python3
"""Module that define a class Student"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not isinstance(type(attrs) is list and all(type(attr) is str for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__