import unittest
from unittest.mock import patch, Mock
from pymath import multiply


class TestMultiplyFunction(unittest.TestCase):
    
    def test_overflow(self):
    
        with self.assertLogs('pymath.functions', level='INFO') as log:
            with self.assertRaises(OverflowError):
                multiply(1000, 1001)
        
        self.assertIn("ERROR:pymath.functions:Overflow detected", log.output)
