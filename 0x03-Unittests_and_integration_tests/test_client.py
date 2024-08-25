#!/usr/bin/env python3
"""
This module contains unittests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    This class contains unittests for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        # Arrange
        test_client = GithubOrgClient(org_name)
        expected_return_value = {"login": org_name}
        mock_get_json.return_value = expected_return_value

        # Act
        result = test_client.org

        # Assert
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected_return_value)

if __name__ == '__main__':
    unittest.main()

