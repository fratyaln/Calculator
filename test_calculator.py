import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(Calculator('+', 1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(Calculator('-', 5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(Calculator('*', 3, 4), 12)

    def test_division(self):
        self.assertEqual(Calculator('/', 10, 2), 5)

if __name__ == '__main__':
    unittest.main()