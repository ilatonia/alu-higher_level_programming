#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A rectangle, inheriting from Base.

    Private instance attributes, each with a public getter and setter:
        __width (int): the width, greater than 0.
        __height (int): the height, greater than 0.
        __x (int): the horizontal offset, greater than or equal to 0.
        __y (int): the vertical offset, greater than or equal to 0.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
            x (int): the horizontal offset of the rectangle.
            y (int): the vertical offset of the rectangle.
            id (int): the id of the instance (see Base).

        Raises:
            TypeError: if an attribute is not an integer.
            ValueError: if width or height is not greater than 0, or if
                x or y is less than 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _check_integer(name, value):
        """Raise a TypeError if value is not an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._check_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._check_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self._check_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self._check_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, using x and y offsets."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes of the rectangle.

        Args:
            *args: the new values, in this order: id, width, height, x, y.
            **kwargs: key/value pairs of attributes to assign. It is
                skipped if args exists and is not empty.
        """
        attributes = ("id", "width", "height", "x", "y")
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for attribute, value in kwargs.items():
                if attribute in attributes:
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
