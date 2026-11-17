#!/usr/bin/python3
"""Unit tests for the Rectangle class (models/rectangle.py)."""
import io
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle

INVALID_TYPES = ("2", 2.5, 2.0, None, [2], {}, (2,), {2}, True, 1j)


class RectangleTestCase(unittest.TestCase):
    """Reset the id counter before each test."""

    def setUp(self):
        """Reset the number of objects of Base."""
        Base._Base__nb_objects = 0

    def printed(self, method):
        """Return what a method prints on the standard output."""
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            method()
        return out.getvalue()


class TestRectangleInit(RectangleTestCase):
    """Test cases for the creation of a Rectangle."""

    def test_inheritance(self):
        """Rectangle inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_ids(self):
        """Ids are managed by Base."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)
        self.assertEqual(Rectangle(1, 1).id, 3)

    def test_id_keyword(self):
        """The id can be a keyword argument."""
        self.assertEqual(Rectangle(1, 1, id=9).id, 9)

    def test_attributes(self):
        """All the arguments are assigned."""
        r = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (10, 2, 3, 4, 5))

    def test_default_offsets(self):
        """x and y are 0 by default."""
        r = Rectangle(10, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_keyword_arguments(self):
        """Arguments can be given by name."""
        r = Rectangle(height=3, width=4, y=1, x=2)
        self.assertEqual((r.width, r.height, r.x, r.y), (4, 3, 2, 1))

    def test_private_attributes(self):
        """Attributes are private and not accessible by their dunder name."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)
        self.assertFalse(hasattr(r, "__width"))

    def test_missing_arguments(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_arguments(self):
        """At most 5 arguments are accepted."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_big_values(self):
        """Big integers are accepted."""
        r = Rectangle(10 ** 20, 10 ** 21, 10 ** 22, 10 ** 23)
        self.assertEqual(r.width, 10 ** 20)


class TestRectangleValidation(RectangleTestCase):
    """Test cases for the validation of the attributes."""

    def assert_error(self, error, message, func, *args):
        """Check that func(*args) raises error with message."""
        with self.assertRaises(error) as context:
            func(*args)
        self.assertEqual(str(context.exception), message)

    def test_width_type(self):
        """A width that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                self.assert_error(TypeError, "width must be an integer",
                                  Rectangle, value, 2)

    def test_height_type(self):
        """A height that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                self.assert_error(TypeError, "height must be an integer",
                                  Rectangle, 2, value)

    def test_x_type(self):
        """An x that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                self.assert_error(TypeError, "x must be an integer",
                                  Rectangle, 2, 2, value)

    def test_y_type(self):
        """A y that is not an integer raises a TypeError."""
        for value in INVALID_TYPES:
            with self.subTest(value=value):
                self.assert_error(TypeError, "y must be an integer",
                                  Rectangle, 2, 2, 0, value)

    def test_width_value(self):
        """A width under or equal to 0 raises a ValueError."""
        for value in (0, -1, -100):
            with self.subTest(value=value):
                self.assert_error(ValueError, "width must be > 0",
                                  Rectangle, value, 2)

    def test_height_value(self):
        """A height under or equal to 0 raises a ValueError."""
        for value in (0, -1, -100):
            with self.subTest(value=value):
                self.assert_error(ValueError, "height must be > 0",
                                  Rectangle, 2, value)

    def test_x_value(self):
        """An x under 0 raises a ValueError."""
        for value in (-1, -100):
            with self.subTest(value=value):
                self.assert_error(ValueError, "x must be >= 0",
                                  Rectangle, 2, 2, value)

    def test_y_value(self):
        """A y under 0 raises a ValueError."""
        for value in (-1, -100):
            with self.subTest(value=value):
                self.assert_error(ValueError, "y must be >= 0",
                                  Rectangle, 2, 2, 0, value)

    def test_zero_offsets_are_valid(self):
        """x and y can be 0."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_smallest_sizes_are_valid(self):
        """Width and height can be 1."""
        r = Rectangle(1, 1)
        self.assertEqual((r.width, r.height), (1, 1))

    def test_validation_order(self):
        """Attributes are validated in the order width, height, x, y."""
        self.assert_error(TypeError, "width must be an integer",
                          Rectangle, "a", "b", "c", "d")
        self.assert_error(ValueError, "width must be > 0",
                          Rectangle, 0, "b")
        self.assert_error(TypeError, "height must be an integer",
                          Rectangle, 10, "2")
        self.assert_error(ValueError, "height must be > 0",
                          Rectangle, 10, 0, "c")
        self.assert_error(TypeError, "x must be an integer",
                          Rectangle, 10, 2, "c", "d")
        self.assert_error(ValueError, "y must be >= 0",
                          Rectangle, 10, 2, 3, -1)

    def test_type_is_checked_before_value(self):
        """The type is validated before the value."""
        self.assert_error(TypeError, "width must be an integer",
                          Rectangle, -1.5, 2)

    def test_setters_type(self):
        """Setters raise a TypeError for values that are not integers."""
        r = Rectangle(10, 2, 3, 4)
        for name in ("width", "height", "x", "y"):
            for value in INVALID_TYPES:
                with self.subTest(name=name, value=value):
                    with self.assertRaises(TypeError) as context:
                        setattr(r, name, value)
                    self.assertEqual(str(context.exception),
                                     "{} must be an integer".format(name))

    def test_setters_value(self):
        """Setters raise a ValueError for values out of range."""
        r = Rectangle(10, 2, 3, 4)
        for name, value, message in (
                ("width", 0, "width must be > 0"),
                ("width", -10, "width must be > 0"),
                ("height", 0, "height must be > 0"),
                ("height", -2, "height must be > 0"),
                ("x", -1, "x must be >= 0"),
                ("y", -1, "y must be >= 0")):
            with self.subTest(name=name, value=value):
                with self.assertRaises(ValueError) as context:
                    setattr(r, name, value)
                self.assertEqual(str(context.exception), message)

    def test_setters_keep_old_value_on_error(self):
        """An invalid value does not change the attribute."""
        r = Rectangle(10, 2, 3, 4)
        for name in ("width", "height", "x", "y"):
            with self.assertRaises((TypeError, ValueError)):
                setattr(r, name, -5)
            with self.assertRaises((TypeError, ValueError)):
                setattr(r, name, "5")
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 3, 4))

    def test_setters_valid_values(self):
        """Setters assign valid values."""
        r = Rectangle(10, 2, 3, 4)
        r.width = 1
        r.height = 5
        r.x = 0
        r.y = 9
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 5, 0, 9))

    def test_id_is_not_validated(self):
        """The id has no validation."""
        self.assertEqual(Rectangle(1, 1, 0, 0, "id").id, "id")
        self.assertEqual(Rectangle(1, 1, 0, 0, -5).id, -5)


class TestRectangleArea(RectangleTestCase):
    """Test cases for Rectangle.area."""

    def test_area(self):
        """The area is width multiplied by height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_smallest_area(self):
        """The smallest area is 1."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_big_area(self):
        """Big areas are computed."""
        self.assertEqual(Rectangle(10 ** 10, 10 ** 10).area(), 10 ** 20)

    def test_area_ignores_offsets(self):
        """x and y do not change the area."""
        self.assertEqual(Rectangle(3, 2, 10, 10).area(), 6)

    def test_area_after_change(self):
        """The area follows changes of width and height."""
        r = Rectangle(3, 2)
        r.width = 5
        r.height = 4
        self.assertEqual(r.area(), 20)

    def test_area_with_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(3, 2).area(1)


class TestRectangleDisplay(RectangleTestCase):
    """Test cases for Rectangle.display."""

    def test_display(self):
        """The rectangle is printed with #."""
        self.assertEqual(self.printed(Rectangle(4, 6).display),
                         "####\n" * 6)
        self.assertEqual(self.printed(Rectangle(2, 2).display), "##\n##\n")

    def test_smallest_display(self):
        """A rectangle of 1 by 1 is a single #."""
        self.assertEqual(self.printed(Rectangle(1, 1).display), "#\n")

    def test_wide_and_tall(self):
        """Width and height are not mixed up."""
        self.assertEqual(self.printed(Rectangle(5, 1).display), "#####\n")
        self.assertEqual(self.printed(Rectangle(1, 3).display), "#\n#\n#\n")

    def test_display_with_x_and_y(self):
        """The x offset adds spaces and the y offset adds new lines."""
        self.assertEqual(self.printed(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.printed(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")

    def test_display_with_x_only(self):
        """Only the x offset."""
        self.assertEqual(self.printed(Rectangle(2, 1, 3).display), "   ##\n")

    def test_display_with_y_only(self):
        """Only the y offset."""
        self.assertEqual(self.printed(Rectangle(2, 1, 0, 2).display),
                         "\n\n##\n")

    def test_display_after_change(self):
        """The display follows changes of the attributes."""
        r = Rectangle(1, 1)
        r.width = 2
        r.height = 2
        r.x = 1
        self.assertEqual(self.printed(r.display), " ##\n ##\n")

    def test_display_returns_none(self):
        """The method prints and returns None."""
        with patch("sys.stdout", new_callable=io.StringIO):
            self.assertIsNone(Rectangle(1, 1).display())

    def test_display_with_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)


class TestRectangleStr(RectangleTestCase):
    """Test cases for Rectangle.__str__."""

    def test_str(self):
        """The format is [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_print(self):
        """print uses __str__."""
        self.assertEqual(self.printed(lambda: print(Rectangle(1, 2, 3, 4))),
                         "[Rectangle] (1) 3/4 - 1/2\n")

    def test_str_after_change(self):
        """The string follows changes of the attributes."""
        r = Rectangle(1, 1)
        r.width = 7
        r.y = 3
        self.assertEqual(str(r), "[Rectangle] (1) 0/3 - 7/1")

    def test_format_and_repr(self):
        """format uses __str__."""
        self.assertEqual("{}".format(Rectangle(1, 1)),
                         "[Rectangle] (1) 0/0 - 1/1")


class TestRectangleUpdateArgs(RectangleTestCase):
    """Test cases for Rectangle.update with no-keyword arguments."""

    def test_update_each_argument(self):
        """Each argument is assigned in the order id, width, height, x, y."""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_without_arguments(self):
        """Without argument, nothing changes."""
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")

    def test_extra_arguments_are_ignored(self):
        """Arguments after the fifth are ignored."""
        r = Rectangle(1, 1)
        r.update(5, 4, 3, 2, 1, 99, 100)
        self.assertEqual(str(r), "[Rectangle] (5) 2/1 - 4/3")

    def test_id_can_be_any_value(self):
        """The id has no validation."""
        r = Rectangle(1, 1)
        r.update(None)
        self.assertIsNone(r.id)
        r.update("abc")
        self.assertEqual(r.id, "abc")

    def test_update_validation(self):
        """Values are validated like in the setters."""
        r = Rectangle(10, 10, 10, 10)
        for args, error, message in (
                ((1, "2"), TypeError, "width must be an integer"),
                ((1, 0), ValueError, "width must be > 0"),
                ((1, 2, "3"), TypeError, "height must be an integer"),
                ((1, 2, -3), ValueError, "height must be > 0"),
                ((1, 2, 3, "4"), TypeError, "x must be an integer"),
                ((1, 2, 3, -4), ValueError, "x must be >= 0"),
                ((1, 2, 3, 4, "5"), TypeError, "y must be an integer"),
                ((1, 2, 3, 4, -5), ValueError, "y must be >= 0")):
            with self.subTest(args=args):
                with self.assertRaises(error) as context:
                    r.update(*args)
                self.assertEqual(str(context.exception), message)

    def test_update_returns_none(self):
        """The method returns None."""
        self.assertIsNone(Rectangle(1, 1).update(1))


class TestRectangleUpdateKwargs(RectangleTestCase):
    """Test cases for Rectangle.update with key-worded arguments."""

    def test_update_kwargs(self):
        """Keys are assigned to the matching attributes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_each_key(self):
        """Every attribute can be updated alone."""
        r = Rectangle(1, 1)
        r.update(id=7)
        r.update(width=2)
        r.update(height=3)
        r.update(x=4)
        r.update(y=5)
        self.assertEqual(str(r), "[Rectangle] (7) 4/5 - 2/3")

    def test_order_is_not_important(self):
        """The order of keys does not matter."""
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        r1.update(id=5, width=2, height=3, x=4, y=5)
        r2.update(y=5, x=4, height=3, width=2, id=5)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_kwargs_skipped_if_args(self):
        """Keyword arguments are skipped when there are arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, height=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(1, 2, width=50, y=50)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 2/10")

    def test_unknown_keys_are_ignored(self):
        """Keys that are not attributes are ignored."""
        r = Rectangle(1, 1)
        r.update(color="red", size=3)
        self.assertFalse(hasattr(r, "color"))
        self.assertFalse(hasattr(r, "size"))
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_kwargs_validation(self):
        """Values are validated like in the setters."""
        r = Rectangle(10, 10, 10, 10)
        with self.assertRaises(TypeError) as context:
            r.update(width="2")
        self.assertEqual(str(context.exception), "width must be an integer")
        with self.assertRaises(ValueError) as context:
            r.update(y=-1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_update_with_no_values(self):
        """Without values, nothing changes."""
        r = Rectangle(10, 10, 10, 10)
        r.update(**{})
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangleToDictionary(RectangleTestCase):
    """Test cases for Rectangle.to_dictionary."""

    def test_dictionary(self):
        """The dictionary has id, width, height, x and y."""
        d = Rectangle(10, 2, 1, 9).to_dictionary()
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_type(self):
        """The result is a dict."""
        self.assertIs(type(Rectangle(1, 1).to_dictionary()), dict)

    def test_keys(self):
        """The dictionary only contains the 5 attributes."""
        self.assertEqual(set(Rectangle(1, 1).to_dictionary()),
                         {"id", "width", "height", "x", "y"})

    def test_new_dictionary_each_time(self):
        """Changing the dictionary does not change the instance."""
        r = Rectangle(1, 1)
        d = r.to_dictionary()
        d["width"] = 50
        self.assertEqual(r.width, 1)
        self.assertIsNot(r.to_dictionary(), d)

    def test_after_change(self):
        """The dictionary follows changes of the attributes."""
        r = Rectangle(1, 1)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.to_dictionary(), {"id": 5, "width": 6,
                                             "height": 7, "x": 8, "y": 9})

    def test_round_trip_with_update(self):
        """The dictionary can be used to update another instance."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_dictionary_with_argument(self):
        """The method takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
