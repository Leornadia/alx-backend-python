#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def main():
    """Print wait_random return values."""
    print(await wait_random())
    print(await wait_random(5))
    print(await wait_random(15))

asyncio.run(main()) 
