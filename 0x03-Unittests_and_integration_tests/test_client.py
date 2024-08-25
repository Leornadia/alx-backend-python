#!/usr/bin/env python3
"""
Unittests for the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for the GithubOrgClient class.
    """

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """
        Test the _public_repos_url method.
        """
        test_org = 'google'
        test_payload = {
            "id": 133345,
            "name": "google",
            "public_repos": 123,
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mock_org.return_value = test_payload
        client = GithubOrgClient(test_org)
        self.assertEqual(client._public_repos_url, test_payload["repos_url"])
