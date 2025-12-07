import unittest
from src.analysis import classify_text


class TestClassifyText(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(classify_text(""), "empty")

    def test_whitespace_only(self):
        self.assertEqual(classify_text("     \n\t  "), "empty")

    def test_email_only(self):
        self.assertEqual(classify_text("info@ejemplo.com"), "email_only")

    def test_email_with_spaces(self):
        self.assertEqual(classify_text("   info@ejemplo.com   "), "email_only")

    def test_short_text(self):
        self.assertEqual(classify_text("Hola mundo"), "short")

    def test_exactly_nine_words(self):
        text = "uno dos tres cuatro cinco seis siete ocho nueve"
        self.assertEqual(classify_text(text), "short")

    def test_long_text(self):
        text = "palabra " * 50
        self.assertEqual(classify_text(text.strip()), "long")

    def test_normal_text(self):
        text = "Este es un texto de prueba con contenido de tamaño intermedio."
        self.assertEqual(classify_text(text), "normal")

    def test_email_inside_text(self):
        text = "Puedes escribirme a info@ejemplo.com si tienes dudas"
        self.assertEqual(classify_text(text), "short")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            classify_text(1234)
