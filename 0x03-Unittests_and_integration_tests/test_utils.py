#!/usr/bin/env python3
""" Module for testing utils.py
"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


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
