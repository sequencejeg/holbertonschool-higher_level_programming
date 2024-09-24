#!usr/bin/python3
"""This module contains a function 
    that returns the list of available
    attributes and methods of an object.
"""
def lookup(obj):
    """The `lookup` function returns a list of attributes and methods of the input object.
    :param obj: The `obj` parameter in the `lookup` function is expected to be any Python object for
    which you want to retrieve a list of attributes and methods. The function `dir(obj)` is used to
    return a list of valid attributes and methods for the given object
    :return: The `lookup` function is returning a list of attributes and methods associated with the
    object `obj`.
    """
    return dir(obj)
