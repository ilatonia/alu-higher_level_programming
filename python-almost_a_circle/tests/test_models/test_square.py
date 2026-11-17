#!/usr/bin/python3
"""Unit tests for the Square class (models/square.py)."""
import io
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

INVALID_TYPES = ("2", 2.5, 2.0, None, [2], {}, (2,), {2}, True, 1j)


class SquareTestCase(unittest.TestCase):
    """Reset the id counter before each test."""

    def setUp(self):
        """Reset the number of objects of Base."""
        Base._Base__nb_objects = 0

    def printed(self, method):
        """Return what a method prints on the standard output."""
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            method()
        return out.getvalue()


class TestSquareInit(SquareTestCase):
    """Test cases for the creation of a Square."""

    def test_inheritance(self):
        """Square inherits from Rectangle and from Base."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))
        self.assertIsInstance(Square(1), Rectangle)
        self.assertIsInstance(Square(1), Base)

    def test_ids(self):
        """Ids are managed by Base."""
        self.assertEqual(Square(5).id, 1)
        self.assertEqual(Square(2, 2).id, 2)
        self.assertEqual(Square(3, 1, 3).id, 3)
        self.assertEqual(Square(3, 1, 3, 12).id, 12)
        self.assertEqual(Square(1).id, 4)

    def test_id_keyword(self):
        """The id can be a keyword argument."""
        self.assertEqual(Square(1, id=9).id, 9)

    def test_attributes(self):
        """The size is the width and the height."""
        s = Square(5, 2, 3, 7)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 5, 2, 3, 7))

    def test_default_offsets(self):
        """x and y are 0 by default."""
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_no_new_attribute(self):
        """A Square only has the attributes of a Rectangle."""
        self.assertEqual(set(vars(Square(5))),
                         set(vars(Rectangle(5, 5))))

    def test_missing_argument(self):
        """The size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_arguments(self):
        """At most 4 arguments are accepted."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_methods_of_rectangle_are_inherited(self):
        """Methods are inherited from Rectangle."""
        self.assertIs(Square.area, Rectangle.area)
        self.assertIs(Square.display, Rectangle.display)


class TestSquareValidation(SquareTestCase):
    """Test cases for the validation of the attributes."""

    def test_size_type(self):
        """A size that is not an integer raises a width TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    Square(value)
                self.assertEqual(str(context.exception),
                                 "width must be an integer")

    def test_size_value(self):
        """A size under or equal to 0 raises a width ValueError."""
        for value in (0, -1, -100):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as context:
                    Square(value)
                self.assertEqual(str(context.exception),
                                 "width must be > 0")

    def test_x_type(self):
        """An x that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    Square(2, value)
                self.assertEqual(str(context.exception),
                                 "x must be an integer")

    def test_y_type(self):
        """A y that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    Square(2, 0, value)
                self.assertEqual(str(context.exception),
                                 "y must be an integer")

    def test_x_value(self):
        """An x under 0 raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Square(2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_y_value(self):
        """A y under 0 raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            Square(2, 0, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_validation_order(self):
        """Attributes are validated in the order size, x, y."""
        with self.assertRaises(TypeError) as context:
            Square("a", "b", "c")
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(TypeError) as context:
            Square(1, "b", "c")
        self.assertEqual(str(context.exception), "x must be an integer")
        with self.assertRaises(ValueError) as context:
            Square(1, 0, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_zero_offsets_are_valid(self):
        """x and y can be 0."""
        s = Square(1, 0, 0)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_x_and_y_setters(self):
        """The setters of x and y validate their values."""
        s = Square(5)
        s.x = 3
        s.y = 4
        self.assertEqual((s.x, s.y), (3, 4))
        with self.assertRaises(TypeError):
            s.x = "3"
        with self.assertRaises(ValueError):
            s.y = -4
        self.assertEqual((s.x, s.y), (3, 4))


class TestSquareSize(SquareTestCase):
    """Test cases for the size getter and setter."""

    def test_getter(self):
        """The size is the width."""
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        """The setter assigns the width and the height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_setter_type(self):
        """A size that is not an integer raises a width TypeError."""
        s = Square(5)
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                with self.assertRaises(TypeError) as context:
                    s.size = value
                self.assertEqual(str(context.exception),
                                 "width must be an integer")

    def test_setter_value(self):
        """A size under or equal to 0 raises a width ValueError."""
        s = Square(5)
        for value in (0, -1):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as context:
                    s.size = value
                self.assertEqual(str(context.exception),
                                 "width must be > 0")

    def test_setter_keeps_old_value_on_error(self):
        """An invalid size does not change the square."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"
        self.assertEqual((s.width, s.height), (5, 5))

    def test_width_and_height_can_be_changed(self):
        """Width and height are inherited attributes."""
        s = Square(5)
        s.width = 6
        self.assertEqual(s.size, 6)


class TestSquareArea(SquareTestCase):
    """Test cases for the area of a Square."""

    def test_area(self):
        """The area is the size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_smallest_area(self):
        """The smallest area is 1."""
        self.assertEqual(Square(1).area(), 1)

    def test_area_after_size_change(self):
        """The area follows the size."""
        s = Square(2)
        s.size = 6
        self.assertEqual(s.area(), 36)


class TestSquareDisplay(SquareTestCase):
    """Test cases for the display of a Square."""

    def test_display(self):
        """The square is printed with #."""
        self.assertEqual(self.printed(Square(5).display), "#####\n" * 5)

    def test_display_with_x(self):
        """The x offset adds spaces."""
        self.assertEqual(self.printed(Square(2, 2).display), "  ##\n  ##\n")

    def test_display_with_x_and_y(self):
        """The y offset adds new lines."""
        self.assertEqual(self.printed(Square(3, 1, 3).display),
                         "\n\n\n ###\n ###\n ###\n")

    def test_smallest_display(self):
        """A square of size 1 is a single #."""
        self.assertEqual(self.printed(Square(1).display), "#\n")

    def test_display_after_size_change(self):
        """The display follows the size."""
        s = Square(1)
        s.size = 2
        self.assertEqual(self.printed(s.display), "##\n##\n")


class TestSquareStr(SquareTestCase):
    """Test cases for Square.__str__."""

    def test_str(self):
        """The format is [Square] (<id>) <x>/<y> - <size>."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")
        self.assertEqual(str(Square(4, 5, 6, 7)), "[Square] (7) 5/6 - 4")

    def test_print(self):
        """print uses __str__."""
        self.assertEqual(self.printed(lambda: print(Square(1, 2, 3))),
                         "[Square] (1) 2/3 - 1\n")

    def test_str_after_change(self):
        """The string follows changes of the attributes."""
        s = Square(1)
        s.size = 8
        s.x = 2
        self.assertEqual(str(s), "[Square] (1) 2/0 - 8")


class TestSquareUpdateArgs(SquareTestCase):
    """Test cases for Square.update with no-keyword arguments."""

    def test_update_each_argument(self):
        """Each argument is assigned in the order id, size, x, y."""
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_without_arguments(self):
        """Without argument, nothing changes."""
        s = Square(5)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_extra_arguments_are_ignored(self):
        """Arguments after the fourth are ignored."""
        s = Square(5)
        s.update(9, 8, 7, 6, 5, 4)
        self.assertEqual(str(s), "[Square] (9) 7/6 - 8")

    def test_size_sets_width_and_height(self):
        """The size argument updates both sides."""
        s = Square(5)
        s.update(1, 9)
        self.assertEqual((s.width, s.height), (9, 9))

    def test_update_validation(self):
        """Values are validated like in the setters."""
        s = Square(5)
        for args, error, message in (
                ((1, "2"), TypeError, "width must be an integer"),
                ((1, 0), ValueError, "width must be > 0"),
                ((1, 2, "3"), TypeError, "x must be an integer"),
                ((1, 2, -3), ValueError, "x must be >= 0"),
                ((1, 2, 3, "4"), TypeError, "y must be an integer"),
                ((1, 2, 3, -4), ValueError, "y must be >= 0")):
            with self.subTest(args=args):
                with self.assertRaises(error) as context:
                    s.update(*args)
                self.assertEqual(str(context.exception), message)


class TestSquareUpdateKwargs(SquareTestCase):
    """Test cases for Square.update with key-worded arguments."""

    def test_update_kwargs(self):
        """Keys are assigned to the matching attributes."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_each_key(self):
        """Every attribute can be updated alone."""
        s = Square(1)
        s.update(id=7)
        s.update(size=2)
        s.update(x=3)
        s.update(y=4)
        self.assertEqual(str(s), "[Square] (7) 3/4 - 2")

    def test_order_is_not_important(self):
        """The order of keys does not matter."""
        s1 = Square(1)
        s2 = Square(1)
        s1.update(id=5, size=2, x=3, y=4)
        s2.update(y=4, x=3, size=2, id=5)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_kwargs_skipped_if_args(self):
        """Keyword arguments are skipped when there are arguments."""
        s = Square(5)
        s.update(89, size=1, x=2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 5")

    def test_unknown_keys_are_ignored(self):
        """Keys that are not attributes are ignored."""
        s = Square(5)
        s.update(color="red")
        self.assertFalse(hasattr(s, "color"))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_kwargs_validation(self):
        """Values are validated like in the setters."""
        s = Square(5)
        with self.assertRaises(TypeError) as context:
            s.update(size="2")
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(ValueError) as context:
            s.update(x=-1)
        self.assertEqual(str(context.exception), "x must be >= 0")


class TestSquareToDictionary(SquareTestCase):
    """Test cases for Square.to_dictionary."""

    def test_dictionary(self):
        """The dictionary has id, size, x and y."""
        self.assertEqual(Square(10, 2, 1).to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_type(self):
        """The result is a dict."""
        self.assertIs(type(Square(1).to_dictionary()), dict)

    def test_keys(self):
        """The dictionary only contains the 4 attributes."""
        self.assertEqual(set(Square(1).to_dictionary()),
                         {"id", "size", "x", "y"})

    def test_new_dictionary_each_time(self):
        """Changing the dictionary does not change the instance."""
        s = Square(1)
        d = s.to_dictionary()
        d["size"] = 50
        self.assertEqual(s.size, 1)

    def test_after_change(self):
        """The dictionary follows changes of the attributes."""
        s = Square(1)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.to_dictionary(),
                         {"id": 5, "size": 6, "x": 7, "y": 8})

    def test_round_trip_with_update(self):
        """The dictionary can be used to update another instance."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)

    def test_dictionary_with_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
