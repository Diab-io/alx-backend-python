#!/usr/bin/env python3
""" Testing client module """
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
    def test_org(self, org: str, res: Dict, mock_org) -> None:
        """
        tests output of org
        """
        mock_org.return_value = MagicMock(return_value=res)
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org(), res)

        mock_org.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """ used for testing public repos url """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as client_org_mock:
            client_org_mock.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_json: MagicMock) -> None:
        """ Test for the pucblic repo method """
        test_payload = {
            'repos_url': "https://api.github.com/users/amazon/repos",
            'repos': [
                {
                    "id": 432248,
                    "name": "amazon.aws",
                    "owner": {
                        "login": "amazon",
                        "id": 322234,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/amazon/amazon.aws",
                    "created_at": "2022-07-23T00:24:37Z",
                    "updated_at": "2023-11-15T11:53:58Z",
                    "has_issues": True,
                    "forks": 8,
                    "default_branch": "master",
                },
                {
                    "id": 54983945,
                    "name": "giftshop",
                    "private": False,
                    "owner": {
                        "login": "amazon",
                        "id": 347567443,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/amazon/giftshop",
                    "created_at": "2017-06-01T22:52:33Z",
                    "updated_at": "2023-04-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 10,
                    "default_branch": "master",
                },
            ]
        }
        mock_json.return_value = test_payload["repos"]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pub_url:
            mock_pub_url.return_value = test_payload["repos_url"]
            self.assertAlmostEqual(
                GithubOrgClient("amazon").public_repos(),
                ['amazon.aws', 'giftshop']
            )
            mock_pub_url.assert_called_once()
        mock_json.assert_called_once()
