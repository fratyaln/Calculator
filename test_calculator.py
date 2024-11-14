import unittest
from Calculator import calculator

class TestCalculator(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculator('+', 1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(calculator('-', 5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculator('*', 3, 4), 12)

    def test_division(self):
        self.assertEqual(calculator('/', 10, 2), 5)

if __name__ == '__main__':
    unittest.main()
