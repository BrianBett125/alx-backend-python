#!/usr/bin/env python3
"""
A co-routine function called async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    A co-routine function called async_generator
    Generates 10 numbers at regular interval
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
