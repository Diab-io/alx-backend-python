#!/usr/bin/env python3
""" creating concurrent coroutines  """


import asyncio
from typing import List

wait_rand = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of delays """
    task = [asyncio.create_task(wait_rand(max_delay)) for i in range(n)]
    sort_task = [await tasks for tasks in asyncio.as_completed(task)]
    return sort_task
