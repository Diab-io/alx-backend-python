#!/usr/bin/env python3
""" A coroutine that takes no args """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ A coroutine that creates an async generator """
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
