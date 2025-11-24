#!/usr/bin/env python3
"""Module that define a function
asynchron"""
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """Fonction that wait a random time between
     0 and 10 and return it"""
    x = random.uniform(0.0, max_delay)
    await asyncio.sleep(x)
    return x
