#!/usr/bin/env python3
""" A basic async syntax """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ A coroutine that waits a specified amoount of time """
    wait_sec = random.uniform(0, max_delay)
    await asyncio.sleep(wait_sec)
    return wait_sec
