import unittest
from src.analysis import normalize_text


class TestNormalizeText(unittest.TestCase):

    def test_basic_text(self):
        self.assertEqual(normalize_text("¡Hola, Mundo!"),
                         "hola mundo")

    def test_extra_spaces_and_case(self):
        self.assertEqual(normalize_text("   Esto   es   UNA   Prueba   "),
                         "esto es una prueba")

    def test_only_punctuation(self):
        self.assertEqual(normalize_text("!!!...,,,;;;"), "")

    def test_mixed_content(self):
        self.assertEqual(normalize_text("¡Hola! ¿Qué tal? Bien... gracias."),
                         "hola qué tal bien gracias")

    def test_raises_typeerror_if_not_str(self):
        with self.assertRaises(TypeError):
            normalize_text(123)
