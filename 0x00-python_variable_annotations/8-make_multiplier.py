#!/usr/bin/env python3
"""This module contains a function to create a multiplier function."""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a number by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float as input and
                                 returns the result of multiplying it by
                                 the multiplier.
    """

    def inner_multiplier(number: float) -> float:
        """
        Multiplies the input number by the captured multiplier.
        """
        return number * multiplier

    return inner_multiplier

