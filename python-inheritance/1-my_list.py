#!/usr/bin/python3
"""Module that defines MyList, a subclass of list."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
