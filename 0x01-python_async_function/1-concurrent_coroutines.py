#!/usr/bin/env python3
" concurrent coroutine module """
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ An async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay. You will
    spawn wait_random n times with the specified
    max_delay"""
    delays = []
    tasks = []

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
