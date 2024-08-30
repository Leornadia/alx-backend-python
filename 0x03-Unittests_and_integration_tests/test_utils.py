#!/usr/bin/env python3
"""
Unit tests for utils module functions.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns correct results."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for missing keys."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns expected JSON response."""
        with patch('utils.requests.get') as mock_get:
            # Set up the mock to return the test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Check that requests.get was called once with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Check that the result is the expected payload
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    class TestClass:
        """Class to test memoization."""
        
        def a_method(self):
            """Method that returns 42."""
            return 42

        @memoize
        def a_property(self):
            """Memoized property that returns a_method result."""
            return self.a_method()

    def test_memoize(self):
        """Test that a_method is called only once with memoize."""
        with patch.object(self.TestClass, 'a_method', return_value=42) as mock_method:
            obj = self.TestClass()

            # Call a_property twice
            result1 = obj.a_property
            result2 = obj.a_property

            # Verify that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Verify that a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()

