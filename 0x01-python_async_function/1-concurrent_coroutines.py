#!/usr/bin/env python3
""" creating concurrent coroutines  """

from typing import List

wait_rand = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """ returns a list of delays """
    delays = []
    for i in range(0, n):
        delay = await wait_rand(max_delay)
        delays.append(delay)

    return sorted(delays)
