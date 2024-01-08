#!/usr/bin/env python3
""" Multiple coroutines """
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ takes 2 args, n & max_delay then returns the list of delays """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    # Creating a list of task objects, each will run wait_random concurrently
    completed_tasks = await asyncio.gather(*tasks)
    # Awaiting the completion of all the tasks and gathering their results
    return completed_tasks
    # Returning the list of completed tasks' results (delays)
