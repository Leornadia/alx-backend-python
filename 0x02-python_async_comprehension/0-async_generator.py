#!/usr/bin/env python3
"""
Module that defines an asynchronous generator
"""
import asyncio
import random

async def async_generator() -> float:
    """
    An asynchronous generator that yields random numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
