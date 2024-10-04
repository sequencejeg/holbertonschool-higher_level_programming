#!/usr/bin/python3

"""
This class extends the built-in
list class in Python.
"""


class MyList(list):
    """
    A custom list class that inherits
    from the built-in list class.

    This class provides an additional method, print_sorted,
    which prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        The function `print_sorted` prints
        the sorted elements of a given list.
        """
        print(sorted(self))
