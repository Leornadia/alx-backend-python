#!/usr/bin/env python3
"""Async Generator module."""

import asyncio
import random

async def async_generator():
    """
    Coroutine that yields 10 random numbers between 0 and 10.
    Each yield is preceded by an asynchronous wait of 1 second.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
