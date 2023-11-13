import unittest
from calc import add, sub, multiply, division

x = float(input("first number: "))
y = float(input("second number: "))

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(x, y), x + y)

    def test_subtract(self):
        self.assertEqual(sub(x, y), x - y)

    def test_multiply(self):
        self.assertEqual(multiply(x, y), x * y)

    def test_division(self):
        self.assertEqual(division(x, y), x / y)

        with self.assertRaises(ValueError):
            division(x, 0)

if __name__ == '__main__':
    unittest.main()
