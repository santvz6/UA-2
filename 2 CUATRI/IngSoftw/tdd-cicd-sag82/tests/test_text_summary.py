import unittest
from src.analysis import text_summary


class TestTextSummary(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(text_summary(""),
                         {"chars": 0, "words": 0, "lines": 0})

    def test_single_line(self):
        self.assertEqual(text_summary("Hola mundo"),
                         {"chars": 10, "words": 2, "lines": 1})

    def test_multiple_lines(self):
        text = "Hola mundo\nSegunda línea\nTercera"
        self.assertEqual(text_summary(text),
                         {"chars": len(text), "words": 5, "lines": 3})

    def test_ignores_empty_lines(self):
        text = "Primera línea\n\nSegunda\n\n"
        self.assertEqual(text_summary(text),
                         {"chars": len(text), "words": 3, "lines": 2})

    def test_only_spaces(self):
        text = "     "
        self.assertEqual(text_summary(text),
                         {"chars": 5, "words": 0, "lines": 0})

    def test_trailing_and_leading_whitespace(self):
        text = "   Hola mundo   \n"
        self.assertEqual(text_summary(text),
                         {"chars": len(text), "words": 2, "lines": 1})

    def test_raises_typeerror_if_not_str(self):
        with self.assertRaises(TypeError):
            text_summary(1234)
        with self.assertRaises(TypeError):
            text_summary(None)
