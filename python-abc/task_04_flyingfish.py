#!/usr/bin/python3
"""
This module defines a simple class hierarchy to demonstrate
multiple inheritance in Python using Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """ A class representing a fish """
    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the fish's natural habitat.
        """
        print("The fish lives in water")


class Bird:
    """ A class representing a bird """
    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the bird's natural habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish, which inherits from both Fish and Bird.
    """
    def fly(self):
        """
        Print a message indicating the flying fish is soaring.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Print a message indicating the flying fish is swimming.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Print a message indicating the flying fish's dual habitat.
        """
        print("The flying fish lives both in water and the sky!")
