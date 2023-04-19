# test_day_01_part_02.py
import unittest
from day_01_part_02 import fuel_required

class TestFuelRequired(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel_required(14), 2)
        self.assertEqual(fuel_required(1969), 966)
        self.assertEqual(fuel_required(100756), 50346)

if __name__ == '__main__':
    unittest.main()
    