#!/usr/bin/env python3

import asyncio
from random import uniform

async def wait_random(max_delay=10):
    """
    Asynchronous coroutine that waits for a random delay
    between 0 and max_delay (inclusive) and returns that delay.
    
    Args:
        max_delay (int): The maximum delay time in seconds. Default is 10.
    
    Returns:
        float: A random float value representing the delay.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n, max_delay):
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay and returns the list of delays
    sorted in ascending order.
    
    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay time for each call.
    
    Returns:
        List[float]: A list of delays in ascending order.
    """
    # Create a list of tasks for wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    
    # Await the completion of all tasks
    delays = await asyncio.gather(*tasks)
    
    # Insert delays in a new list to maintain order without using sort()
    sorted_delays = []
    for delay in delays:
        # Insert the delay into the sorted list
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)  # Add to the end if it's the largest
    
    return sorted_delays
