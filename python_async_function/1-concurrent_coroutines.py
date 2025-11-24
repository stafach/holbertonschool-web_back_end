#!/usr/bin/env python3
"""Module that defines a function that
call wait_random funciont n time with delay"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that return a list of max_delay"""
    i : int = 0
    coroutines = [wait_random(max_delay) for i in range(n)]
    delays: List[float] = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
