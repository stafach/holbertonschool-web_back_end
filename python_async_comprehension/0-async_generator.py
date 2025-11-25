#!/usr/bin/env python3
"""Module that create a function async"""

import asyncio
import random


async def async_generator():
    """Function that will loop 10 times, each
    time asynchronously wait 1 second, then
    yield a random number between 0 and 10"""
    i: int = 0
    for i in range(10):
        await asyncio.sleep(1)
        delay: float = random.uniform(0, 10)
        yield delay
