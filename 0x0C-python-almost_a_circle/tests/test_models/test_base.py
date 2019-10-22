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

    def test_basic_case(self):
        self.assertEqual(max_integer([1, 2, 3, 6]), 6)
        self.assertEqual(max_integer([5, 6, 1, 8]), 8)
        self.assertEqual(max_integer([21, 23, 32, 71]), 71)

    def text_negative_case(self):
        self.assertEqual(max_integer([-1, -2, -3, -6]), -6)
        self.assertEqual(max_integer([-5, -6, -1, -8, -2]), -1)
        self.assertEqual(max_integer([21, 23, 32, 71]), -71)

    def test_basic_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_basic_float(self):
        self.assertEqual(max_integer([0.65, 2.4, 3.0]), 3.0)
        self.assertEqual(max_integer([12.9, 8.1, 8.0]), 12.9)
        self.assertEqual(max_integer([11.2, 5.6, 20.1, 15.3]), 20.1)

    def test_basic_oneelement(self):
        self.assertEqual(max_integer([1]), 1)

    def test_basic_string(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
