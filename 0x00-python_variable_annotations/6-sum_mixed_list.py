#!/usr/bin/env python3
"""A type-annotated function that recieves a  mixed value list and sums"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """ Sums the list which has both int and float and return float """
    return sum(mxd_lst)
