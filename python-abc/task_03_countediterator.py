#!/usr/bin/python3
"""This module defines the CountedIterator class."""


class CountedIterator:
    """A custom iterator that counts the number of elements
    retrieved during iteration."""
    def __init__(self, obj):
        """Initialize the CountedIterator."""
        self.count = 0
        self.iterator = iter(obj)

    def get_count(self):
        """Return the number of elements that have been iterated over."""
        return self.count

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item
