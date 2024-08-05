#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine named wait_n.
"""
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
  """
  Spawns wait_random n times with the specified max_delay.

  Args:
      n (int): The number of times to spawn wait_random.
      max_delay (int): The maximum delay for each wait_random call.

  Returns:
      list: A list of all the delays in ascending order.
  """
  tasks = [wait_random(max_delay) for _ in range(n)]
  return [await task for task in asyncio.as_completed(tasks)]
