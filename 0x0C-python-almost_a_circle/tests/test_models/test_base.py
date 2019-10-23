#!/usr/bin/python3
"""
creating “Interactive tests”. Test for taht base.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Test_BaseClass(unittest.TestCase):
    """
    unittest base test class.
    """

     def test_standard(self):
        b1 = Base(12); b2 = Base(-45)
        b3 = Base(); b4 = Base()
        self.assertEqual(b1.id, 12); self.assertEqual(b2.id, -45)
        self.assertEqual(type(b3.id), int); self.assertEqual(type(b4.id), int)

    def test_not_int_id(self):
        b1 = Base([2, 3, 4])
        self.assertEqual(b1.id, [2, 3, 4])
        b2 = Base("Wasabi")
        self.assertEqual(b2.id, "Wasabi")

    def test_conflicting_id(self):
        b1 = Base()
        b2 = Base(1)
        self.assertEqual(type(b1.id), int)
        self.assertEqual(b2.id, 1)

    def test_reg_dict_to_string(self):
        b = Base()
        tmpDict = {'x': 1, 'y': 8, 'id': 1, 'height': 3, 'width': 9}
        self.assertEqual(type(b.to_json_string(tmpDict)), str)

    def test_emptyDict(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")

    def test_from_toDict_to_str(self):
        r = Rectangle(10, 15, 13, 37, id=55)
        self.assertEqual(type(r.to_dictionary()), dict)

    def test_fromJsonStr(self):
        b = Base()
        tmpDictStr = "{\"x\": 1, \"width\": 8, \"id\": 4, \"height\": 6, \"y\": 8}"
        self.assertEqual(type(b.from_json_string(tmpDictStr)), dict)
        tmpDictStr = "[{\"x\": 1, \"width\": 8, \"id\": 4, \"height\": 6, \"y\": 8}]"
        self.assertEqual(type(b.from_json_string(tmpDictStr)), list)

    def test_fromJsonStr_wit_empty_str(self):
        b = Base()
        self.assertEqual(type(b.from_json_string(None)), list)
