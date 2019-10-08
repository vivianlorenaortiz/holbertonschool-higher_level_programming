#!/usr/bin/python3


"""
8-rectangle.py: creates a Rectangle class
"""


class Rectangle:
    """
    Rectangle class.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            fruit += (str(self.print_symbol) * self.width)
            if rows != self.height - 1:
                fruit += '\n'
            rows += 1
        return fruit

    def __del__(self):
        """
        Message gets printed when a Rectangle instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

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
