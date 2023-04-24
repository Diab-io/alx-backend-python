#!/usr/bin/env python3
"""Files used to test nested map function"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
import json


class TestAccessNestedMap(unittest.TestCase):
    """Test class for testing the function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method to check if the expected output is gotten"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test to check if a keyError is raised"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class that handles all test cases of the get_json method"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test the get_json method using a mock object"""
        mockBehavior = {'json.return_value': payload}
        attrs = Mock(**mockBehavior)
        with patch('utils.requests.get', return_value=attrs) as mocked_get:
            self.assertEqual(get_json(url), payload)
            mocked_get.assert_called_once_with(url)
