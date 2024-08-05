#!/usr/bin/env python3
"""
2-measure_runtime.py

This module defines a function to measure the runtime of wait_n.
"""

import time
import asyncio
from typing import List
from 1_concurrent_coroutines import wait_n

async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per call.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        float: The average time per call.
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

