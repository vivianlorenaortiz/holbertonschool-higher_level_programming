#!/usr/bin/python3
class Student:


def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for key, value in self._dict_.items():
                if key in attrs:
                    new_dic[key] = value

            return nre_dic
