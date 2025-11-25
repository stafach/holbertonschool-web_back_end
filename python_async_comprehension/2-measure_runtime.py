#!/usr/bin/env python3
"""Module that create a function that
call async_comprehension"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """Coroutine that execute async_comprehension four
    times in parallel using asyncio.gather and measure
    the total runtime and return it"""

    i: int = 0
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()

    runtime = end - start
    return runtime
