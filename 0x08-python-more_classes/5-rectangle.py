#!/usr/bin/python3


"""
5-rectangle.py: creates a Rectangle class
"""


class Rectangle:
    """
    Rectangle class.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle
        """
        self.width = width
        self.height = height

    def __repr__(self):
        """
        Returns a string representation of an instance of Rectangle
        """
        fruit = "Rectangle({}, {})".format(self.width, self.height)
        return fruit

    def __str__(self):
        """
        Returns string representation of a Rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        fruit = ""
        rows = 0
        while rows < self.height:
            fruit += ("#" * self.width)
            if rows != self.height - 1:
                fruit += '\n'
            rows += 1
        return fruit

    def __del__(self):
        """
        Message gets printed when a Rectangle instance is deleted
        """
        print("Bye rectangle...")

    def area(self):
        """
        Returns the area of a Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of a Rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value
