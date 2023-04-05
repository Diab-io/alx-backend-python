#!/usr/bin/env python3
""" A coroutine that takes no argument """

import asyncio
from typing import List

generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """returns numbers comprehended from the gen."""
    return [comp async for comp in generator()]
