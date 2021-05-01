import unittest
from main import Calculator
import json


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.test_class = Calculator()
        self.data = {}

        with open('fixtures_test_class.json', encoding='utf8') as f:
            self.data = json.load(f)

    def test_calculate_sum(self):
        for v in self.data['sum']:
            self.assertEqual(self.test_class.sum(v[0], v[1]), v[2])

    def test_calculate_mult(self):
        for v in self.data['mult']:
            self.assertEqual(self.test_class.mult(v[0], v[1]), v[2])


if __name__ == "__main__":
    unittest.main()
