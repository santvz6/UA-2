import unittest

from pymath import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -5), -7)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_both_sign_numbers(self):
        self.assertEqual(add(3, -5), -2)

