#!/usr/bin/env python3
"""
This module provides a function to calculate the length of each element in a
list of sequences.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in a list of sequences.

    Args:
        lst (Iterable[Sequence]): The list of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
                                     a sequence from the input list and its length.
    """
    return [(i, len(i)) for i in lst]
