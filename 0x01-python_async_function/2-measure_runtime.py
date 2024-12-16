#!/usr/bin/env python3
""" 2-measure runtime module """
from typing import List
import time
import asyncio
import importlib.util


module_path = './1-concurrent_coroutines.py'

spec = importlib.util.spec_from_file_location('module_name', module_path)
module = importlib.util.module_from_spec(spec)

spec.loader.exec_module(module)

wait_n = module.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure_time function that returns sorted lists containing
       max_delay random values
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
