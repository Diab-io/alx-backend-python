#!/usr/bin/env python3
""" Creation of an asynchronous task """
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio:
    """ returns an asynchronous task """
    created_task = asyncio.create_task(wait_random(max_delay))
    return created_task
