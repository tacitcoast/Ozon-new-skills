import unittest
from main import calculate_credit


class TestCalculator(unittest.TestCase):

    def test_calculate_numbers(self):
        # sum, procemt, month
        self.assertEqual(calculate_credit(100000, 0.05, 12), 8560)
        self.assertIsNone(calculate_credit(100000, 0, 12), 8560)
        self.assertIsNone(calculate_credit(100000, 0.05, 0))
        self.assertEqual(calculate_credit(0, 0.05, 12), 0)


if __name__ == "__main__":
    unittest.main()
