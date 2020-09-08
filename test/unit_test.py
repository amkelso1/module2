"""
Author: Alex Kelso
Program: camper_age_input.py
last date modified: 9/9/2020

program that accepts an integer value for years and returns an integer representing months
"""


import unittest
from main import camper_main_input


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(72, camper_main_input.convert_to_months(6))


if __name__ == '__main__':
    unittest.main()
