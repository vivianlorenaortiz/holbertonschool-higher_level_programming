#!/usr/bin/python3
class Student:

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new_dic = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dic[key] = value

            return new_dic

    def reload_from_json(self, json):
        if json is not None:
            if "first_name" in json:
                self.first_name = json["first_name"]
            if "last_name" in json:
                self.last_name = json["last_name"]
            if "age" in json:
                self.age = json["age"]
