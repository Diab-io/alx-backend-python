#!/usr/bin/env python3
"""Type-annotated function that has params of different types"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple that contains a string and the square of the 2nd param"""
    return k, v**2
