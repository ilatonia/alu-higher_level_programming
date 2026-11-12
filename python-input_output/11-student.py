#!/usr/bin/python3
"""Module that defines the Student class with serialization support."""


class Student:
    """A student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student.

        Args:
            first_name (str): the first name.
            last_name (str): the last name.
            age (int): the age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        Args:
            attrs (list): if it is a list of strings, only the attributes
                whose names are in this list are retrieved. Otherwise all
                attributes are retrieved.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the Student from a dictionary.

        Args:
            json (dict): maps each public attribute name to its value.
        """
        for key, value in json.items():
            setattr(self, key, value)
