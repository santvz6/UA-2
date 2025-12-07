import unittest
from src.basic import count_lines


class TestCountLines(unittest.TestCase):
    def test_multiple_lines(self):
        self.assertEqual(count_lines("Hola\nmega\nmundo"), 3)

    def test_lines_with_empty(self):
        self.assertEqual(count_lines("Hola\n\nmundo"), 2)

    def test_trailing_newline(self):
        self.assertEqual(count_lines("Hola\nmundo\n"), 2)

    def test_empty_string(self):
        self.assertEqual(count_lines(""), 0)

    def test_single_space(self):
        self.assertEqual(count_lines(" "), 0)

    def test_single_newline(self):
        self.assertEqual(count_lines("\n"), 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            count_lines(123)
