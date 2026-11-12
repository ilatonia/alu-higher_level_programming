#!/usr/bin/python3
"""Module that defines the append_write function."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    The file is created if it does not exist.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
