#!/usr/bin/env python3
""" A coroutine that takes no argument """

import asyncio

generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """returns numbers comprehended from the gen."""
    comps = [comp async for comp in generator()]
    return comps
