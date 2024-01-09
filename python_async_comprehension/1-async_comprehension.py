#!/usr/bin/env python3
""" collects 10 random numbers using async
returns 10 random numbers"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ Collects 10 random numbers then returns it """
    # Returns 10 numbers collected, we ar iterating
    return [i async for i in async_generator()]
