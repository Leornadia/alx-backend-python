#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of a list containing
integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
        float: The sum of the elements in the list.
    """
    total: float = 0.0
    for element in mxd_lst:
        total += element
    return total
