import unittest
from pymath import divide


class TestDivideFunction(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(6, 3), 2)
        
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)


