#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """The max is the last element of an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """The max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """The max is somewhere in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 5, 2, 4]), 5)

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_duplicates(self):
        """Repeated values are handled."""
        self.assertEqual(max_integer([3, 3, 3]), 3)
        self.assertEqual(max_integer([1, 4, 4, 2]), 4)

    def test_negative_numbers(self):
        """The max of negative numbers is the closest to zero."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Negative, zero and positive numbers are compared correctly."""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, 0, -3]), 0)

    def test_floats(self):
        """Floats are compared correctly."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_integers_and_floats(self):
        """Integers and floats can be mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)
        self.assertEqual(max_integer([3, 2.5, 2]), 3)

    def test_big_numbers(self):
        """Very big integers are handled."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 19, 1]), 10 ** 20)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling the function without argument returns None."""
        self.assertIsNone(max_integer())

    def test_list_is_not_modified(self):
        """The list is left untouched."""
        numbers = [3, 1, 2]
        max_integer(numbers)
        self.assertEqual(numbers, [3, 1, 2])

    def test_tuple(self):
        """A tuple works like a list."""
        self.assertEqual(max_integer((1, 5, 2)), 5)

    def test_strings(self):
        """Strings are compared alphabetically."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types(self):
        """Elements that cannot be compared raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])
        with self.assertRaises(TypeError):
            max_integer([None, 1])

    def test_not_a_list(self):
        """Arguments without a length raise a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
