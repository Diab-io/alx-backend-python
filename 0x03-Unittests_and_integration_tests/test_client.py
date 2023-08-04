#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from typing import Dict
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Test org in GithubOrgClient
    """
    @parameterized.expand([
        ('google', {'login': "google"}),
        ('abc', {'login': "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org: str, res: Dict, mock_org):
        """
        tests output of org
        """
        mock_org.return_value = MagicMock(return_value=res)
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org(), res)

        mock_org.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as client_org_mock:
            client_org_mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
