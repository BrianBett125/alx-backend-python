#!/usr/bin/env python3
"""
test_client module
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient class."""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        test_org method
        Test the org() method of GithubOrgClient.

        Arguments:
        - org_name: The organization name to test for
        - mock_get_json: Mock object for get_json() method
        """
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}'
                )

    def test_public_repos_url(self):
        """Test the public_repos_url property."""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload
            test_client = GithubOrgClient('test')
            result = test_client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos() method."""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "hello/world"
            test_client = GithubOrgClient('test')
            result = test_client.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test for GithubOrgClient.has_license() method."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class using fixtures."""

    @classmethod
    def setUpClass(cls):
        """
        setupClass method
        Set up the test class before each method."""
        conf = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **conf)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        test_public_repos method
        Test the public_repos() method with integration."""
        test_client = GithubOrgClient("google")

        self.assertEqual(test_client.org, self.org_payload)
        self.assertEqual(test_client.repos_payload, self.repos_payload)
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        test_public_repos_with_license method
        Test the public_repos() method with integration and license."""
        test_client = Github
