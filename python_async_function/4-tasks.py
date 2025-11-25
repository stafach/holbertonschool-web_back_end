#!/usr/bin/env python3
"""Module that create a function that
call task_wait_random"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that return a list of max_delay"""
    i: int = 0
    coroutines = [task_wait_random(max_delay) for i in range(n)]
    delays: List[float] = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
