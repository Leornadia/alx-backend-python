#!/usr/bin/env python3
"""
Module that defines an async comprehension
"""
from typing import List
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    An async comprehension that returns a list of random numbers
    """
    random_numbers = [i async for i in async_generator()]
    return random_numbers
