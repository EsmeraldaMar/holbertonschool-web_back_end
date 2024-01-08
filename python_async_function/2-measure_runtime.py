#!/usr/bin/env python3
""" Measures runtime function """
import asyncio
import random
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Takes 2 args n & max_delay measures runtime """
    start_time = time.perf_counter()
    # run the async function 'wait_n'
    asyncio.run(wait_n(n, max_delay))
    # Calculate the elapsed time
    time_process = time.perf_counter() - start_time
    # Return the average time per operation
    return time_process / n
