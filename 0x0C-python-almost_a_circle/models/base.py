#!/usr/bin/python3
"""
This module contains the "Base" class
"""

import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save as json file"""
        if list_objs is not None:
            empty_list = []
            for i in list_objs:
                empty_list.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as New_file:
            New_file.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ list of the JSON string"""
        if json_string is None or json_string is "":
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes"""
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 2)
        elif cls.__name__ is "Square":
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances """
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
