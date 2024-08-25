#!/usr/bin/env python3
"""
This module contains unittests and integration tests for main.py.
"""

import unittest
from main import add_numbers, multiply_numbers

class TestMain(unittest.TestCase):
    """
    This class contains unittests for functions in main.py.
    """

    def test_add_numbers(self):
        """
        Test that add_numbers correctly adds two numbers.
        """
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_multiply_numbers(self):
        """
        Test that multiply_numbers correctly multiplies a list of numbers.
        """
        self.assertEqual(multiply_numbers([1, 2, 3]), 6)
        self.assertEqual(multiply_numbers([0, 1, 2]), 0)
        self.assertEqual(multiply_numbers([2, 5]), 10)

class TestIntegration(unittest.TestCase):
    """
    This class contains integration tests for the project.
    """

    def test_add_and_multiply(self):
        """
        Test the integration of add_numbers and multiply_numbers.
        """
        sum_result = add_numbers(1, 2)
        multiply_result = multiply_numbers([sum_result, 2])
        self.assertEqual(multiply_result, 6)

if __name__ == '__main__':
    unittest.main()
