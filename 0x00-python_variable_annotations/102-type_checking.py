#!/usr/bin/env python3
"""
This module provides a function to zoom an array.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zooms an array by a given factor.

    Args:
        lst (Tuple): The array to zoom.
        factor (int, optional): The zoom factor. Defaults to 2.

    Returns:
        Tuple: The zoomed array.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)  # Return as a tuple
