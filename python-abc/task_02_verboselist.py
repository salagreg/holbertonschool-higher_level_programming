#!/usr/bin/python3
"""
This module defines the `VerboseList` class, which extends Python's
built-in `list` type.
The class overrides common list modification methods
('append', 'extend', 'remove', and 'pop')
to print descriptive messages whenever these methods are used.
"""


class VerboseList(list):
    """
    A subclass of the built-in list that overrides certain methods
    to print verbose output when the list is modified.
    """
    def append(self, item):
        """
        Add an item to the end of the list with a message.
        """
        print(f"Added {[item]} to the list.")
        super().append(item)

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable,
        with a message.
        """
        print(f"Extended the list with {list(iterable)} items.")
        super().extend(iterable)

    def remove(self, item):
        """
        Remove the first occurrence of a value from the list, with a message.
        """
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at the given position, with a message.
        """
        item = super().pop(index)
        print(f"Popped {[item]} from the list.")
        return item
