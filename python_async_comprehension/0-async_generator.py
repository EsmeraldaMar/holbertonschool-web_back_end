#!/usr/bin/env python3
""" Created async generator, no args, loops 10 times and waits 1 second"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """ Loops 10 times, yields random num """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
