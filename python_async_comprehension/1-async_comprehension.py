#!/usr/bin/env python3
"""Module that create a function that
call async_generator"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Corutine that collect 10 random numbers
    then return the 10 random numbers."""
    result: List[float] = []

    async for i in async_generator():
        result.append(i)

    return result
