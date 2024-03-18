#!/usr/bin/env python3
"""
* From the previous file, import wait_n into 2-measure_runtime.py.

* Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
Your function should return a float.

* Use the time module to measure an approximate elapsed time.
"""
from asyncio import run
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_runtime(n: int, max_delay: int) -> float:
    """Returns the timeTaken to run a task"""
    start_time = perf_counter()
    await wait_n(n, max_delay)
    end_time = perf_counter()
    elapsed_time = end_time - start_time

    return elapsed_time/n


def measure_time(n: int, max_delay: int) -> float:
    return run(measure_runtime(n, max_delay))
