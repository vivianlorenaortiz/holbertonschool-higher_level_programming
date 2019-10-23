#!/usr/bin/python3
""" exercise rectangle.py. """
from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    def __str__(self):
        """
        __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def area(self):
        """
            Calculates area
        """
        return self.width * self.height

    def display(self):
        """
            displays
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print((self.__x * " ") + (self.__width * "#"))

    def to_dictionary(self):
        """
            to dict
        """
        new_dict = self.__dict__
        n = {}
        n["width"] = new_dict["_Rectangle__width"]
        n["heidht"] = new_dict["_Rectangle__height"]
        n["id"] = new_dict["id"]
        n["x"] = new_dict["_Rectangle__x"]
        n["y"] = new_dict["_Rectangle__y"]
        return n

    def update(self, *args, **kwargs):
        """
            update the class
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def width(self):
        """
        getter
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        setter
        """
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """
        height
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        height setter
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """
        getter
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        setter
        """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """
        getter
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        setter
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val
