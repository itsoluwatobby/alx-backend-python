#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function
task_wait_n. The code is nearly identical to wait_n except
task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    it asynchronously spawns `task_wait_random` n times with a
    specified max_delay.

    Returns a list of delays.
    """
    delays_list = []
    for _ in range(n):
        delay: List[float] = await task_wait_random(max_delay)
        delays_list.append(delay)
    return delays_list
