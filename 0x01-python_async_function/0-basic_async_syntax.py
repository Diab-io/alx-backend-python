#!/usr/bin/env python3
""" A basic async syntax """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> (int|float):
    """ A coroutine that waits a specified amoount of time """
    wait_sec = random.uniform(0, max_delay+1)
    await asyncio.sleep(wait_sec)
    return wait_sec
