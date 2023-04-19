# test_day_01_part_01.py
import unittest
from day_01_part_01 import fuel_required

class TestFuelRequired(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel_required(12), 2)
        self.assertEqual(fuel_required(14), 2)
        self.assertEqual(fuel_required(1969), 654)
        self.assertEqual(fuel_required(100756), 33583)

if __name__ == '__main__':
    unittest.main()
