#!/usr/bin/python3
"""Module that defines a Square class with a string description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private size."""

    def __init__(self, size):
        """Initialize a Square.

        Args:
            size (int): the side length, a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description: [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
