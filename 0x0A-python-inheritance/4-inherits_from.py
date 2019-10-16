#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ returns True if the object in an instance of a class
    that inherited (directly or indirectly) from a specified class """
    if issubclass(type(obj), a_class) and type(obj) is a_class:
        return False
    else:
        return True
