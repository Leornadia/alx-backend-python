#!/usr/bin/env python3

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of a number.

    Args:
        k (str): A string to be used as the first element of the tuple.
        v (Union[int, float]): A number (int or float) to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the input string
        and the second element is the square of the input number as a float.
    """
    return (k, float(v ** 2))
