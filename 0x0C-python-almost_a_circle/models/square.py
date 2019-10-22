#!/usr/bin/python3
""" square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format \
        (self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """
        to dict
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """
        update square
        """
        tmpArr = ["id", "size", "x", "y"]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for x, arg in enumerate(args):
            setattr(self, tmpArr[x], arg)

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, val):
        self.width = val
        self.height = val
