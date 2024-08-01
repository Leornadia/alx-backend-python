#!/usr/bin/env python3

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list of float numbers to sum.

    Returns:
        float: The sum of all numbers in the input list.
    """
    return sum(input_list)
