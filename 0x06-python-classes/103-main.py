#!/usr/bin/python3

import unittest
import math
from 103-magic_class import MagicClass

class TestMagicClass(unittest.TestCase):

    def test_constructor_with_valid_radius(self):
        radius = 5
        magic_instance = MagicClass(radius)
        self.assertEqual(magic_instance._MagicClass__radius, radius)

    def test_constructor_with_invalid_radius_type(self):
        with self.assertRaises(TypeError):
            magic_instance = MagicClass('invalid_radius')

    def test_area_calculation(self):
        radius = 3
        magic_instance = MagicClass(radius)
        expected_area = math.pi * radius ** 2
        self.assertEqual(magic_instance.area(), expected_area)

    def test_circumference_calculation(self):
        radius = 4
        magic_instance = MagicClass(radius)
        expected_circumference = 2 * math.pi * radius
        self.assertEqual(magic_instance.circumference(), expected_circumference)

if __name__ == '__main__':
    unittest.main()

