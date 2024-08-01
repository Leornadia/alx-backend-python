#!/usr/bin/env python3
"""This module contains a function to add the float/int numbers of a list."""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a list containing both integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of all numbers in the list, as a float.
    """
    total = 0.0
    for num in mxd_lst:
        total += float(num)
    return total

