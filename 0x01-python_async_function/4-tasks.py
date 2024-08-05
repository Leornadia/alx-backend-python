#!/usr/bin/env python3
"""
Module that contains the task_wait_n function
"""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive).

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a asyncio.Task that will execute wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The asyncio.Task object.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for each wait_random call.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    delays = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        delays.append(await task)
    return delays
