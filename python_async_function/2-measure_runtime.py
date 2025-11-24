#!/usr/bin/env python3
"""Module that measures the execution time of wait_n"""

import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time of wait_n(n, max_delay)
    and returns the average time per coroutine.
    This is a normal function (not async) so it can be called directly.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()

    total_time: float = end - start
    return total_time / n
