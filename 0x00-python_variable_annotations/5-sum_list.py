#!/usr/bin/env python3
"""A type-annotated function that returns the sum of all vals in list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return the sum of the list values """
    return sum(input_list)
