#!/usr/bin/python3
"""
This module defines a custom class MyList that inherits from the built-in list.
"""


class MyList(list):
    """ MyList class that inherits from the built-in list """
    def print_sorted(self):
        """ Prints the list in ascending sorted order """
        print(sorted(self))
