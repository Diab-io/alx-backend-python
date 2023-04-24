#!/usr/bin/env python3
"""Files used to test nested map function"""
from parameterized import parameterized
from typing import Dict, List, Union
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
import json


class TestAccessNestedMap(unittest.TestCase):
    """Test class for testing the function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: str,
                               expected: Union[Dict, int]):
        """Test method to check if the expected output is gotten"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: str,
                                         expected: Exception):
        """Test to check if a keyError is raised"""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class that handles all test cases of the get_json method"""
    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        """Test the get_json method using a mock object"""
        mockBehavior = {'json.return_value': payload}
        attrs = Mock(**mockBehavior)
        with patch('requests.get', return_value=attrs) as mocked_get:
            self.assertEqual(get_json(url), payload)
            mocked_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """class that tests memoize function"""
    def test_memoize(self):
        """tests what is returned from memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=lambda: 42) as memo:
            testClass = TestClass()
            self.assertEqual(testClass.a_property(), 42)
            self.assertEqual(testClass.a_property(), 42)
            memo.assert_called_once()
