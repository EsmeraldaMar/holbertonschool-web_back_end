#!/usr/bin/env python3
""" Takes code wait_n, alter to new func task_wait_n """
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ takes 2 args, n & max_delay then returns the list of delays """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_tasks = await asyncio.gather(*tasks)
    # Awaiting the completion of all the tasks and gathering their results
    return sorted(completed_tasks)
    # Returning the list of completed tasks' results (delays)
