#!/usr/bin/env python3
"""Async Generator module."""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields 10 random numbers between 0 and 10.

    Each number is generated concurrently after waiting for 1 second.
    """

    async def generate_random_number():
        """Helper coroutine to generate a random number after 1 second."""
        await asyncio.sleep(1)
        return random.uniform(0, 10)

    tasks = [asyncio.create_task(generate_random_number()) for _ in range(10)]
    for task in asyncio.as_completed(tasks):
        yield await task
