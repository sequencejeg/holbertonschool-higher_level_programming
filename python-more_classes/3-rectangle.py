#!/usr/bin/python3

"""This is a class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """initializes a new rectangle

        Args:
            width (int, optional): Sets the width of the rectangle.
            Defaults to 0.
            height (int, optional): Sets the height of the rectangle.
            Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """sets the current width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the current rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the current height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the current height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)
