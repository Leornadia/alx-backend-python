#!/usr/bin/env python3
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random with the specified max_delay.

    Args:
    max_delay (int): The maximum delay in seconds.

    Returns:
    asyncio.Task: A task that will execute wait_random(max_delay).
    """
    return asyncio.create_task(wait_random(max_delay))