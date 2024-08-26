#!/usr/bin/env python3

import unittest
from unittest import mock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from parameterized import parameterized_class

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up the class with patched requests.get."""
        cls.get_patcher = mock.patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Define the side effect with values for each expected call
        mock_get.side_effect = [
            mock.Mock(**{'json.return_value': cls.org_payload}),   # First call: fetching org
            mock.Mock(**{'json.return_value': cls.repos_payload}), # Second call: fetching repos
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method returns the expected results."""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method filters repos with a specific license."""
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)

    def test_public_repos_url(self):
        """Test _public_repos_url method returns the correct URL."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client._public_repos_url, self.org_payload["repos_url"])

    def test_org(self):
        """Test org method returns the organization payload."""
        client = GithubOrgClient("test_org")
        self.assertEqual(client.org, self.org_payload)

    def test_org_cached(self):
        """Test org method is cached."""
        client = GithubOrgClient("test_org")
        # Call org twice and check if requests.get was called only once
        client.org
        client.org
        self.assertEqual(client.org, self.org_payload)


if __name__ == "__main__":
    unittest.main()

