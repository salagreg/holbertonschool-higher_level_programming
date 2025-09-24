#!/usr/bin/python3
"""
This module defines an abstract base class `Animal` using Python's abc module.
"""


from abc import ABC, abstractmethod

class Animal(ABC):
  """Abstract base class representing an animal."""


  @abstractmethod
  def sound(self):
      """Abstract method that must be implemented by all subclasses."""
      pass
  
class Dog(Animal):
    """Dog class that implements the sound method."""


    def sound(self):
      return "Bark"
    

class Cat(Animal):
    """Cat class that implements the sound method."""

    
    def sound(self):
      return "Meow"
