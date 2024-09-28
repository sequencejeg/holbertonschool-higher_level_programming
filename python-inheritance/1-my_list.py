#!/usr/bin/python3

"""
This class extends the built-in
list class in Python.
"""


class MyList(list):
    def print_sorted(self):
        """
        The function `print_sorted` prints
        the sorted elements of a given list.
        """
        print(sorted(self))
