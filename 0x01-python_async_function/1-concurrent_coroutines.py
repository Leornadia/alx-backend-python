#!/usr/bin/env python3
import asyncio
from typing import List
from wait_random import wait_random  # Ensure you have the correct import for wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for wait_random.

    Returns:
        List[float]: A list of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Instead of sorting, we can use a simple method to insert and maintain order
    sorted_delays = []
    for delay in delays:
        # Insert delay in sorted order
        index = 0
        while index < len(sorted_delays) and sorted_delays[index] < delay:
            index += 1
        sorted_delays.insert(index, delay)

    return sorted_delays

