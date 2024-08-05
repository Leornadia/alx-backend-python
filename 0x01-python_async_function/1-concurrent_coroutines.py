#!/usr/bin/env python3
"""
1-concurrent_coroutines.py

This module defines an asynchronous routine that spawns wait_random n times.
"""

import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns the list of delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)
    return sorted_delays

