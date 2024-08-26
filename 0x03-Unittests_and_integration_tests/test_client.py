#!/usr/bin/env python3
"""
This module contains unittests for the GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """
    This class contains unittests for the GithubOrgClient class.
    """

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct value.
        """
        # Arrange
        test_client = GithubOrgClient("google")
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Act
        result = test_client._public_repos_url

        # Assert
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

if __name__ == '__main__':
    unittest.main()

