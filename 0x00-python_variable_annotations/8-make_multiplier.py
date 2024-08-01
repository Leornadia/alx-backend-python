#!/usr/bin/env python3

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
