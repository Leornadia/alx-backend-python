#!/usr/bin/env python3
"""Async Generator module."""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields 10 random numbers between 0 and 10.

    Each number is generated after waiting for 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
