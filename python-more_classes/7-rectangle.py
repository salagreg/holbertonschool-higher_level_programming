#!/usr/bin/python3
"""Module that defines a Rectangle class with width and height."""


class Rectangle:
    """
    Represents a rectangle defined by its width and height.

    This class provides methods to compute the area,
    and perimeter of the rectangle,
    display it using a customizable symbol,
    and keep track of the number of instances.

    Class Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        print_symbol (any): Symbol used for string representation ('#').

    Instance Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle (2 * (width + height)),
            or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using the '#'.
        Replace a character '#' with a public instance attribute 'print_symbol'

        Returns:
        str: The rectangle represented with lines of '#' characters.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            rect.append(str(self.print_symbol * self.__width))
        return "\n".join(rect)

    def __repr__(self):
        """
        Return a string representation of the Rectangle instance.

        The returned string can be used with eval() to create a new
        instance with the same width and height.

        Returns:
        str: A string in the format "Rectangle(width, height)".
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Called when a Rectangle instance is about to be destroyed.

        Prints a goodbye message and decrements the class attribute
        'number_of_instances' to reflect the deletion of the instance.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
