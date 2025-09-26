#!/usr/bin/python3
"""
This module defines mixins for swimming and flying behaviors,
and a Dragon class that combines both capabilities.
"""


class SwimMixin:
    """
    Mixin class that adds swimming behavior.
    Intended to be used as a base class to add the 'swim' method to another class.
    """
    def swim(self):
        """
        Print a message indicating the creature is swimming.
        """
        print("The creature swims!")
    
class FlyMixin:
    """
    Mixin class that adds flying behavior.
    Intended to be used as a base class to add the 'fly' method to another class.
    """
    def fly(self):
        """
        Print a message indicating the creature is flying.
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon that can both swim and fly,
    by inheriting from SwimMixin and FlyMixin.
    """
    def roar(self):
        """
        Print a message indicating the dragon is roaring.
        """
        print("The dragon roars!")
