# https://github.com/tylerhartmanbiz/lab11-TH-AB
# Partner 1: Tyler Hartman
# Partner 2: Aiden Bascelli


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertAlmostEqual(mul(2.5, 0.4), 1.0)

    def test_divide(self): # 3 assertions
        # div(a, b) returns b / a
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(-4, 20), -5)
        self.assertAlmostEqual(div(3, 1), 0.3333333333)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        # div(a, b) returns b / a, so the divisor is the FIRST argument
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        # logarithm(base, argument)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)

    def test_log_invalid_base(self):
        # logarithm(base, argument): base must be > 0
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-5, 10)

    ######## Partner 1
    def test_log_invalid_argument(self): # 2 assertions
        # logarithm(base, argument): argument must be > 0
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142135624)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(2), 1.4142135624)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()