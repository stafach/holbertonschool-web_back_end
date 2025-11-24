#!/usr/bin/env python3
"""Module that defines an asynchronous function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function that waits a random time between
    0 and max_delay seconds and returns it"""

    x: float = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
