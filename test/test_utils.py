import unittest
from src.utils import Calculator


class TestCalculator(unittest.TestCase):

    def test_mnozenie_dwie_liczby(self):
        c = Calculator(5, 6)
        assert c.mnozenie() == 30

    def test_mnozenie_2_stringi(self):
        c = Calculator('text','text')
        self.assertRaises(TypeError, c.mnozenie)

    def test_mnozenie_string_int(self):
        pass