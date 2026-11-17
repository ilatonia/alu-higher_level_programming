#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square, inheriting from Rectangle.

    A square is a rectangle with the same width and height, so no new
    attribute is created: size is the width (and the height).
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
            x (int): the horizontal offset of the square.
            y (int): the vertical offset of the square.
            id (int): the id of the instance (see Base).

        Raises:
            TypeError: if an attribute is not an integer.
            ValueError: if size is not greater than 0, or if x or y is
                less than 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square (its width and its height)."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assign attributes of the square.

        Args:
            *args: the new values, in this order: id, size, x, y.
            **kwargs: key/value pairs of attributes to assign. It is
                skipped if args exists and is not empty.
        """
        attributes = ("id", "size", "x", "y")
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for attribute, value in kwargs.items():
                if attribute in attributes:
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
