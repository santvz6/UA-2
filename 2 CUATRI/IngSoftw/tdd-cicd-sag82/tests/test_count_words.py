import unittest
from src.basic import count_words


class TestCountWords(unittest.TestCase):
    def test_basic_sentence(self):
        text = "Esto es una prueba"
        self.assertEqual(count_words(text), 4)

    def test_leading_and_trailing_spaces(self):
        text = "   Hola    mundo  "
        self.assertEqual(count_words(text), 2)

    def test_numbers_and_text(self):
        text = "Me he comido 2 bocadillos"
        self.assertEqual(count_words(text), 5)

    def test_symbols_between_words(self):
        text = "2 * 2"
        self.assertEqual(count_words(text), 3)

    def test_multiple_lines(self):
        text = "Hola\nmundo"
        self.assertEqual(count_words(text), 2)

    def test_punctuation_strings(self):
        text = ". , # ~ ó"
        self.assertEqual(count_words(text), 5)

    def test_punctuation_attached(self):
        text = "Hola, mundo. ¿Cómo estáis?"
        self.assertEqual(count_words(text), 4)

    def test_empty_string(self):
        text = ""
        self.assertEqual(count_words(text), 0)

    def test_only_spaces(self):
        text = "     "
        self.assertEqual(count_words(text), 0)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_words(None)
        with self.assertRaises(TypeError):
            count_words(123)
