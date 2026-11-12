#!/usr/bin/python3
"""Module that defines the class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    All attributes of the object's class must be serializable: list,
    dictionary, string, integer or boolean.
    """
    return obj.__dict__
