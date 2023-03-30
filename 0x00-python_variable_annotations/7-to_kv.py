#!/usr/bin/env python3
"""Type-annotated function that has params of different types"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes str and int or float, returns str, square of v as float"""
    return k, v**2
