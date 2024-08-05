#!/usr/bin/env python3
"""
3-tasks.py

This module defines a function that returns an asyncio.Task.
"""

import asyncio
from 0_basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: A task that will run the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))

