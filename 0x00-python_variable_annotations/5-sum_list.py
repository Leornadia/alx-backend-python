#!/usr/bin/env python3
"""This module contains a function to add the float numbers of a list."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of all floats in the input_list.
    """
    total = 0.0
    for num in input_list:
        total += num
    return total


