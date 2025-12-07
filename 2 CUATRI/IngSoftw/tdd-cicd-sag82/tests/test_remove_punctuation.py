import unittest
from src.basic import remove_punctuation


class TestRemovePunctuation(unittest.TestCase):
    def test_basic_punctuation(self):
        text = "Hola, mundo!"
        self.assertEqual(remove_punctuation(text), "Hola mundo")

    def test_multiple_punctuation(self):
        text = "¿Qué tal? ¡Bien, gracias!"
        self.assertEqual(remove_punctuation(text), "Qué tal Bien gracias")

    def test_only_punctuation(self):
        text = "!?.,;:"
        self.assertEqual(remove_punctuation(text), "")

    def test_mixed_with_numbers(self):
        text = "El precio es $100.00, ¿vale?"
        self.assertEqual(remove_punctuation(text), "El precio es 10000 vale")

    def test_no_punctuation(self):
        text = "Solo texto y espacios"
        self.assertEqual(remove_punctuation(text), "Solo texto y espacios")

    def test_empty_string(self):
        text = ""
        self.assertEqual(remove_punctuation(text), "")

    def test_punctuation_inside_words(self):
        text = "co-operar re_evaluar"
        self.assertEqual(remove_punctuation(text), "cooperar reevaluar")

    def test_quotes_and_parentheses(self):
        text = '"Hola (mundo)"'
        self.assertEqual(remove_punctuation(text), "Hola mundo")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_punctuation(123)
        with self.assertRaises(TypeError):
            remove_punctuation(None)
