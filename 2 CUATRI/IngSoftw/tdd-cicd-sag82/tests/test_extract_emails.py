import unittest
from unittest.mock import patch
from src.analysis import extract_emails


class TestExtractEmails(unittest.TestCase):
    def test_single_email(self):
        text = "Contáctame en prueba@example.com"
        result = extract_emails(text)
        self.assertEqual(result, ["prueba@example.com"])

    def test_multiple_emails(self):
        text = "Correos: uno@mail.com, dos@test.org y tres@dominio.net"
        result = extract_emails(text)
        self.assertEqual(result, ["uno@mail.com", "dos@test.org", "tres@dominio.net"])

    def test_no_email(self):
        text = "Este texto no contiene correos"
        #  logger en src/analysis.py
        with self.assertLogs("src.analysis", level="WARNING") as cm:
            result = extract_emails(text)
            self.assertEqual(result, [])
            self.assertTrue(any("WARNING" in message for message in cm.output))

    def test_mixed_content(self):
        text = "Envía a: info@site.com o revisa ejemplo.org para más detalles"
        result = extract_emails(text)
        self.assertEqual(result, ["info@site.com"])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            extract_emails(1234)

    @patch("src.analysis.logger")
    def test_logging_info_called(self, mock_logging):
        text = "a@a.com b@b.com"
        extract_emails(text)
        mock_logging.info.assert_called_with("Se han encontrado 2 correos electrónicos")

    @patch("src.analysis.logger")
    def test_logging_warning_called(self, mock_logging):
        text = "sin correos aquí"
        extract_emails(text)
        mock_logging.warning.assert_called_with("No se encontraron correos electrónicos")
