import unittest
from src.basic import count_letters


class TestCountLetters(unittest.TestCase):
    def test_only_letters(self):
        text = "HolaMundo"
        self.assertEqual(count_letters(text), 9)

    def test_letters_and_numbers(self):
        text = "Hola 123"
        self.assertEqual(count_letters(text), 4)

    def test_letters_and_symbols(self):
        text = "Hola, mundo!"
        self.assertEqual(count_letters(text), 9)

    def test_empty_string(self):
        text = ""
        self.assertEqual(count_letters(text), 0)

    def test_only_symbols(self):
        text = "123!@#$.;"
        self.assertEqual(count_letters(text), 0)

    def test_single_space(self):
        text = " "
        self.assertEqual(count_letters(text), 0)

    def test_single_newline(self):
        text = "\n"
        self.assertEqual(count_letters(text), 0)

    def test_accented_letters(self):
        text = "éïòî"
        self.assertEqual(count_letters(text), 4)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_letters(123)
        with self.assertRaises(TypeError):
            count_letters(None)
