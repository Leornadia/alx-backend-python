#!/usr/bin/env python3
"""Asynchronous coroutine module."""

import asyncio
import random
import time

async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay time.
    """
    delay_time = random.uniform(0, max_delay)
    time.sleep(delay_time)
    return delay_time
