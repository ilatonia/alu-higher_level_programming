#!/usr/bin/python3
"""Module for text_indentation.

Provides a function that prints a text with 2 new lines after each of
the characters '.', '?' and ':'.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each '.', '?' and ':'.

    Spaces at the beginning and at the end of each printed line are removed.

    Args:
        text: the string to print.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
