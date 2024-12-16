#!/usr/bin/env python3
""" task_wait """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n. The code is nearly identical to wait_n
    except task_wait_random is being called.

    It spawns wait_random n times with a specified delay
    between each call
    Arguments:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Return:
        list of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
