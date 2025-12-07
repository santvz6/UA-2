import unittest
from src.analysis import safe_find


class TestSafeFind(unittest.TestCase):
    def test_word_found(self):
        result = safe_find("Hola mundo", "mundo")
        self.assertEqual(result, 5)

    def test_word_not_found_with_fallback(self):
        result = safe_find("Hola mundo", "adiós", fallback="no encontrado")
        self.assertEqual(result, "no encontrado")

    def test_word_not_found_without_fallback(self):
        with self.assertRaises(ValueError):
            safe_find("Hola mundo", "adiós")

    def test_invalid_text_type(self):
        with self.assertRaises(TypeError):
            safe_find(123, "hola")

    def test_invalid_word_type(self):
        with self.assertRaises(TypeError):
            safe_find("hola mundo", 123)

    def test_word_at_start(self):
        result = safe_find("hola mundo", "hola")
        self.assertEqual(result, 0)

    def test_word_at_end(self):
        result = safe_find("esto es una prueba", "prueba")
        self.assertEqual(result, 12)

    def test_case_sensitive(self):
        with self.assertRaises(ValueError):
            safe_find("hola mundo", "Hola")
