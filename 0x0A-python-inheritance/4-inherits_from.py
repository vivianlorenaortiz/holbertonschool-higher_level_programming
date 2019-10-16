#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
   function python   """
    if issubclass(type(obj), a_class) and type(obj) is a_class:
        return False
    else:
        return True
