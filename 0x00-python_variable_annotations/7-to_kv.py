#!/usr/bin/env python3
"""This module contains a function to create a key-value tuple."""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a key-value tuple.

    Args:
        k (str): The key (string).
        v (Union[int, float]): The value (either an integer or a float).

    Returns:
        Tuple[str, float]: A tuple containing the key (str) and
                           the square of the value as a float.
    """
    return (k, float(v**2))

