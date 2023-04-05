#!/usr/bin/env python3
""" function that alters wait_n into a new function """

import asyncio
from typing import List

task_wait = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of delays """
    task = [task_wait(max_delay) for i in range(n)]
    sort_task = [await tasks for tasks in asyncio.as_completed(task)]
    return sort_task
