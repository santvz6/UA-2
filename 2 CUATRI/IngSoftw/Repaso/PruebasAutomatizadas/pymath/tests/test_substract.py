from pymath import substract

import unittest
from unittest.mock import patch

class TestSubstractFunction(unittest.TestCase):
    
    def test_substract_positive_numbres(self):
        self.assertEqual(substract(5, 3), 2)


    @patch("pymath.functions.add")
    def test_substract_without_add(self, mock_add):
        mock_add.return_value = 2 # Simulamos el valor que nos daría add
        self.assertEqual(substract(5, 3), 2) # Hacemos la resta para llamara al "add"
        mock_add.assert_called_once_with(5, -3) # Confirmamos que el mock se llamó con los argumentos 5 y -3

    def test_substract_zero(self):
        self.assertEqual(substract(5, 0), 5)
        #with self.assertLogs as log:
            #self.assertIn()
            

    def test_substract_both_sign_numbers(self):
        self.assertEqual(substract(3, -5), 8)
    
    def test_substract_to_negative(self):
        self.assertEqual(substract(4, 10), -6)
