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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct list of repos
        and that get_json and _public_repos_url are called appropriately.
        """
        # Arrange
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/test_org/repos'
            client = GithubOrgClient('test_org')

            # Act
            result = client.public_repos()

            # Assert
            expected = ['repo1', 'repo2', 'repo3']
            self.assertEqual(result, expected)
            mock_get_json.assert_called_once_with('https://api.github.com/orgs/test_org/repos')
            mock_public_repos_url.assert_called_once()


if __name__ == '__main__':
    unittest.main()

