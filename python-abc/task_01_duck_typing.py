#!/usr/bin/python3
"""
This module defines an abstract base class 'Shape'
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for geometric shapes.
    Requires subclasses to implement area() and perimeter() methods.
    """
    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        This method must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        This method must be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """ Circle shape that inherits from Shape """
    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Return the area of the circle.

        Returns:
            float: Area calculated as π * radius^2.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle.

        Returns:
            float: Perimeter calculated as 2 * π * radius.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ Rectangle shape that inherits from Shape """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Return the perimeter of the rectangle """
        return (self.width + self.height) * 2


def shape_info(obj):
    """ Print the area and perimeter of a shape """
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())


if __name__ == "__main__":
    c = Circle(5)
    r = Rectangle(3, 4)
    shape_info(c)
    shape_info(r)
