#!/usr/bin/env python3
""" coroutine that takes no args but returns runtime """

import asyncio
import time

async_comp = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ measures the runtime of the coroutine """
    start = time.perf_counter()
    await asyncio.gather(async_comp(), async_comp(), async_comp(),
                         async_comp())
    time_elapsed = time.perf_counter() - start
    return time_elapsed
