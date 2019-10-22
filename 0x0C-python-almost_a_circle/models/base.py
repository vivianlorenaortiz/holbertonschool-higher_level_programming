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
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None and len(list_objs) > 0:
            empty_list = []
            for i in list_objs:
                my_dict = i.to_dictionary()
                empty_list.append(my_dict)
            with open(cls.__name__ + ".json", mode='w', encoding="utf-8") as f:
                    f.write(cls.to_json_string(empty_list))
        else:
            with open(cls.__name__ + ".json", mode='w', encoding="utf-8") as f:
                    f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ list of the JSON string"""
        empty_list = []
        if json_string is None:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """instance with all attributes"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

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
