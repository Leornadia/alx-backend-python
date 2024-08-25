#!/usr/bin/env python3
"""
This module contains the main logic for the project.
"""

from typing import List

def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.
    """
    return a + b

def multiply_numbers(numbers: List[int]) -> int:
    """
    Multiplies a list of numbers and returns the result.
    """
    result = 1
    for number in numbers:
        result *= number
    return result

