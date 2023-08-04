#!/usr/bin/env python3
""" Module for testing utils.py
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ class for testing the access nested map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]):
        """ Testing output of the accessmap function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Method for testing that a keyerror is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class used to test the get_json method in utils
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload) -> None:
        with patch('requests.get') as mock_request_get_obj:
            mock_request_get_obj.return_value.json.return_value = test_payload
            res = get_json(test_url)

            self.assertEqual(res, test_payload)

            mock_request_get_obj.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Used for testing memoize
    """
    def test_memoize(self):
        """
        Method used to test memoize output
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()

            mock_a_method.assert_called_once
