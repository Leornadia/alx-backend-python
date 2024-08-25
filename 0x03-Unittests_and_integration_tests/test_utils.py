#!/usr/bin/env python3
"""
This module contains unittests for the get_json function.
"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):
    """
    This class contains unittests for utils.get_json.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected payload.
        """
        with patch('utils.requests.get') as mock_get:
            # Configure the mock to return a response with the test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called once with test_url
            mock_get.assert_called_once_with(test_url)

            # Assert that the result is the expected payload
            self.assertEqual(result, test_payload)

if __name__ == '__main__':
    unittest.main()

