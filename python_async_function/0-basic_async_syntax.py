#!/usr/bin/env python3
"""
Basic Async Syntax
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ Synchronous coroutine that takes integer as argument """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
