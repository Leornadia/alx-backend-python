#!/usr/bin/env python3
"""
This module contains unittests for the memoize decorator.
"""

import unittest
from unittest.mock import patch
from utils import memoize

class TestMemoize(unittest.TestCase):
    """
    This class contains unittests for the utils.memoize decorator.
    """

    def test_memoize(self):
        """
        Test that the memoize decorator caches the result of a method.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method was only called once
            mock_method.assert_called_once()

            # Assert that the result is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

if __name__ == '__main__':
    unittest.main()

