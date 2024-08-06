#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously generates 10 random numbers between 0 and 10.
    Each number is generated after a 1-second delay.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# The following code is for testing the async_generator function
# This should not be included in the actual module file

if __name__ == "__main__":
    async def print_yielded_values():
        result = []
        async for i in async_generator():
            result.append(i)
        print(result)

    asyncio.run(print_yielded_values())

