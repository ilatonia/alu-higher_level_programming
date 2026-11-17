#!/usr/bin/python3
"""Unit tests for the Base class (models/base.py)."""
import json
import os
import tempfile
import unittest
from unittest.mock import patch

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTestCase(unittest.TestCase):
    """Reset the id counter and work in a temporary directory."""

    def setUp(self):
        """Reset the number of objects and move to a temporary directory."""
        Base._Base__nb_objects = 0
        self.old_dir = os.getcwd()
        self.tmp = tempfile.TemporaryDirectory()
        os.chdir(self.tmp.name)

    def tearDown(self):
        """Go back to the old directory and remove the temporary one."""
        os.chdir(self.old_dir)
        self.tmp.cleanup()

    def read(self, filename):
        """Return the content of a file."""
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()


class TestBaseId(BaseTestCase):
    """Test cases for the id attribute of Base."""

    def test_first_id_is_one(self):
        """The first generated id is 1."""
        self.assertEqual(Base().id, 1)

    def test_ids_are_incremented(self):
        """Each new instance without id gets the next id."""
        self.assertEqual([Base().id for _ in range(5)], [1, 2, 3, 4, 5])

    def test_given_id(self):
        """An id given to the constructor is assigned as is."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)

    def test_id_keyword_argument(self):
        """The id can be given as a keyword argument."""
        self.assertEqual(Base(id=7).id, 7)

    def test_explicit_none_id(self):
        """An id of None generates a new id."""
        self.assertEqual(Base(None).id, 1)

    def test_id_type_is_not_checked(self):
        """The type of the id is not tested."""
        self.assertEqual(Base("abc").id, "abc")
        self.assertEqual(Base(3.5).id, 3.5)
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_given_id_does_not_change_counter(self):
        """An explicit id does not use the counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_example_sequence(self):
        """Ids follow the sequence 1, 2, 3, 12, 4."""
        ids = [Base().id, Base().id, Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 2, 3, 12, 4])

    def test_id_is_assignable(self):
        """The id is a public attribute."""
        base = Base()
        base.id = 42
        self.assertEqual(base.id, 42)

    def test_nb_objects_is_private(self):
        """The counter is a private class attribute."""
        self.assertFalse(hasattr(Base, "__nb_objects"))
        self.assertEqual(Base._Base__nb_objects, 0)
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_too_many_arguments(self):
        """The constructor takes at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_subclasses_share_the_counter(self):
        """Rectangle and Square use the counter of Base."""
        self.assertEqual(Rectangle(1, 1).id, 1)
        self.assertEqual(Square(1).id, 2)
        self.assertEqual(Base().id, 3)

    def test_instances_are_independent(self):
        """Two instances do not share the same id."""
        self.assertNotEqual(Base().id, Base().id)


class TestBaseToJsonString(BaseTestCase):
    """Test cases for Base.to_json_string."""

    def test_none(self):
        """None gives an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list gives an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_one_dictionary(self):
        """A list of one dictionary is converted to a string."""
        result = Base.to_json_string([{"id": 1, "width": 10}])
        self.assertEqual(json.loads(result), [{"id": 1, "width": 10}])

    def test_several_dictionaries(self):
        """A list of several dictionaries is converted to a string."""
        data = [{"id": 1, "x": 2}, {"id": 2, "x": 3}, {"id": 3, "x": 4}]
        self.assertEqual(json.loads(Base.to_json_string(data)), data)

    def test_returns_a_string(self):
        """The result is a str."""
        self.assertIs(type(Base.to_json_string([{"id": 1}])), str)
        self.assertIs(type(Base.to_json_string(None)), str)

    def test_exact_format(self):
        """The result is the JSON representation of the list."""
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')
        self.assertEqual(Base.to_json_string([{}]), "[{}]")

    def test_rectangle_dictionary(self):
        """The dictionary of a Rectangle can be converted."""
        dictionary = Rectangle(10, 7, 2, 8).to_dictionary()
        result = Base.to_json_string([dictionary])
        self.assertEqual(json.loads(result), [dictionary])

    def test_no_argument(self):
        """The list is required."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_called_on_an_instance_or_a_subclass(self):
        """The static method works from an instance or a subclass."""
        data = [{"id": 1}]
        self.assertEqual(Base().to_json_string(data), '[{"id": 1}]')
        self.assertEqual(Rectangle.to_json_string(data), '[{"id": 1}]')


class TestBaseFromJsonString(BaseTestCase):
    """Test cases for Base.from_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_list_string(self):
        """The string of an empty list gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_one_dictionary(self):
        """A string with one dictionary gives a list of one dictionary."""
        result = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertEqual(result, [{"id": 89, "width": 10}])

    def test_several_dictionaries(self):
        """A string with several dictionaries gives a list of them."""
        data = [{"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}]
        self.assertEqual(Base.from_json_string(json.dumps(data)), data)

    def test_returns_a_list(self):
        """The result is a list."""
        self.assertIs(type(Base.from_json_string('[{"id": 1}]')), list)
        self.assertIs(type(Base.from_json_string(None)), list)

    def test_round_trip(self):
        """to_json_string and from_json_string are opposite operations."""
        data = [{"id": 89, "width": 10, "height": 4}, {"id": 7, "x": 1}]
        self.assertEqual(
            Base.from_json_string(Base.to_json_string(data)), data)

    def test_invalid_json(self):
        """A string that is not JSON raises a ValueError."""
        with self.assertRaises(ValueError):
            Base.from_json_string("not json")

    def test_no_argument(self):
        """The string is required."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(BaseTestCase):
    """Test cases for Base.save_to_file."""

    def test_rectangles(self):
        """A list of rectangles is saved in Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        content = self.read("Rectangle.json")
        self.assertEqual(
            content,
            Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()]))
        self.assertEqual(json.loads(content), [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}])

    def test_squares(self):
        """A list of squares is saved in Square.json."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        self.assertEqual(json.loads(self.read("Square.json")), [
            {"id": 1, "size": 5, "x": 0, "y": 0},
            {"id": 2, "size": 7, "x": 9, "y": 1}])

    def test_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_empty_list(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        self.assertEqual(self.read("Square.json"), "[]")

    def test_one_object(self):
        """A list of one object is saved."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(len(json.loads(self.read("Rectangle.json"))), 1)

    def test_file_is_overwritten(self):
        """An existing file is overwritten."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        Rectangle.save_to_file([r2])
        self.assertEqual(json.loads(self.read("Rectangle.json")),
                         [r2.to_dictionary()])
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_filename_depends_on_class(self):
        """Each class saves in its own file."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertFalse(os.path.exists("Square.json"))
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_base_with_no_objects(self):
        """Base saves in Base.json."""
        Base.save_to_file(None)
        self.assertEqual(self.read("Base.json"), "[]")
        Base.save_to_file([])
        self.assertEqual(self.read("Base.json"), "[]")

    def test_uses_to_json_string(self):
        """The static method to_json_string is used."""
        r1 = Rectangle(10, 7, 2, 8)
        with patch.object(Base, "to_json_string",
                          return_value='["mock"]') as mock:
            Rectangle.save_to_file([r1])
        mock.assert_called_once_with([r1.to_dictionary()])
        self.assertEqual(self.read("Rectangle.json"), '["mock"]')

    def test_no_argument(self):
        """The list is required."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_objects_without_to_dictionary(self):
        """Objects that cannot be converted raise an AttributeError."""
        with self.assertRaises(AttributeError):
            Base.save_to_file([Base()])


class TestBaseCreate(BaseTestCase):
    """Test cases for Base.create."""

    def test_rectangle(self):
        """A Rectangle is created from its dictionary."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        self.assertEqual(str(r1), str(r2))
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_square(self):
        """A Square is created from its dictionary."""
        s1 = Square(3, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)
        self.assertEqual(str(s1), str(s2))
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_new_instance(self):
        """The result is a new instance, different from the original."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_all_attributes_are_set(self):
        """All the attributes of the dictionary are assigned."""
        r = Rectangle.create(id=89, width=10, height=4, x=2, y=3)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 10, 4, 2, 3))
        s = Square.create(id=7, size=6, x=1, y=2)
        self.assertEqual((s.id, s.size, s.x, s.y), (7, 6, 1, 2))

    def test_partial_dictionary(self):
        """Attributes missing from the dictionary keep a dummy value."""
        r = Rectangle.create(id=89, width=10, height=4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                         (89, 10, 4, 0, 0))

    def test_empty_dictionary(self):
        """Without any value, the dummy instance is returned."""
        self.assertEqual(str(Rectangle.create()), "[Rectangle] (1) 0/0 - 1/1")
        Base._Base__nb_objects = 0
        self.assertEqual(str(Square.create()), "[Square] (1) 0/0 - 1")

    def test_unknown_keys_are_ignored(self):
        """Keys that are not attributes are ignored."""
        r = Rectangle.create(id=5, width=2, height=3, color="red")
        self.assertFalse(hasattr(r, "color"))
        self.assertEqual(str(r), "[Rectangle] (5) 0/0 - 2/3")

    def test_invalid_values(self):
        """Invalid values raise the same errors as the update method."""
        with self.assertRaises(ValueError):
            Rectangle.create(id=1, width=-1, height=2)
        with self.assertRaises(TypeError):
            Square.create(id=1, size="1")

    def test_dummy_instance_uses_an_id(self):
        """The dummy instance consumes an id of the counter."""
        r1 = Rectangle(3, 5, 1)
        Rectangle.create(**r1.to_dictionary())
        self.assertEqual(Rectangle(1, 1).id, 3)


class TestBaseLoadFromFile(BaseTestCase):
    """Test cases for Base.load_from_file."""

    def test_missing_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_rectangles(self):
        """Rectangles are loaded from Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in loaded], [str(r1), str(r2)])
        self.assertEqual([r.to_dictionary() for r in loaded],
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_squares(self):
        """Squares are loaded from Square.json."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual([str(s) for s in loaded], [str(s1), str(s2)])

    def test_returns_list_of_the_right_type(self):
        """The instances are of the class that calls the method."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        Square.save_to_file([Square(1)])
        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()
        self.assertIs(type(rectangles), list)
        self.assertIs(type(rectangles[0]), Rectangle)
        self.assertIs(type(squares[0]), Square)

    def test_new_instances(self):
        """Loaded instances are new objects."""
        r1 = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r1])
        self.assertIsNot(Rectangle.load_from_file()[0], r1)

    def test_empty_files(self):
        """Empty files give an empty list."""
        with open("Rectangle.json", "w") as file:
            file.write("")
        self.assertEqual(Rectangle.load_from_file(), [])
        with open("Square.json", "w") as file:
            file.write("[]")
        self.assertEqual(Square.load_from_file(), [])

    def test_classes_use_their_own_file(self):
        """Square does not read Rectangle.json."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(Square.load_from_file(), [])

    def test_uses_from_json_string_and_create(self):
        """The methods from_json_string and create are used."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with patch.object(Rectangle, "create",
                          return_value="instance") as mock:
            result = Rectangle.load_from_file()
        self.assertEqual(result, ["instance"])
        mock.assert_called_once_with(id=1, width=1, height=2, x=0, y=0)

    def test_example_ids(self):
        """Loading rectangles uses ids that are skipped for next objects."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        Rectangle.load_from_file()
        self.assertEqual(Square(5).id, 5)
        self.assertEqual(Square(7, 9, 1).id, 6)


if __name__ == "__main__":
    unittest.main()
