#!/usr/bin/env python3
"""
This module provides a function to create a tuple with a string and a squared
value.
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Take a string k and an int or float v as arguments and return a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v and should be
    annotated as a float.

    Args:
        k (str): The string to be included in the tuple.
        v (Union[int, float]): The integer or float to be squared and included
                                in the tuple.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return (k, float(v * v))
