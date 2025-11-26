#!/usr/bin/env python3
"""Module that create a function async"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that loops 10 times.
    Each iteration waits 1 second asynchronously,
    then yields a random float between 0 and 10.
    """
    i: int = 0
    for i in range(10):
        await asyncio.sleep(1)
        delay: float = random.uniform(0, 10)
        yield delay
