#!/usr/bin/env python3
"""
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times
with the specified max_delay.
"""
import asyncio
from typing import List
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random
# from '0-basic_async_syntax' import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""
    list_of_delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_of_delays.append(delay)
    return list_of_delays
