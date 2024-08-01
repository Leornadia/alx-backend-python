#!/usr/bin/env python3
"""
This module provides a function that returns a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Take a float multiplier as argument and return a function that multiplies
    a float by multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float by the
                                  input multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier
    return multiplier_function
