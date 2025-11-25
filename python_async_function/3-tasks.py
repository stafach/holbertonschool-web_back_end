#!/usr/bin/env python3
"""Module that import wait_random and return
a asyncion.Task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that return a asyncio.Task"""
    task = asyncio.Task(wait_random(max_delay))

    return task
