#!/usr/bin/python3
"""base.py"""
import json


class Base:
    """ Base Class """

    _nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base._nb_objects += 1
            self.id = Base._nb_objects

        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        lo = []
        if list_objs is not None:
            for x in list_objs:
                lo.append(cls.to_dictionary(x))
        with open(filename, "w+") as f:
            f.write(cls.to_json_string(lo))

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
                    tmp = cls(1, 1)
        elif cls.__name__ is "Square":
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        l = []
        try:
            with open(filename, 'r') as f:
                l = cls.from_json_string(f.read())
            for i, e in enumerate(l):
                l[i] = cls.create(**l[i])
        except:
            pass
        return l
