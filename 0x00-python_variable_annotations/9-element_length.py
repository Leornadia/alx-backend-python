#!/usr/bin/env python3
"""This module contains a function to calculate the length of each element in a sequence."""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in an iterable of sequences.

    Args:
        lst (Iterable[Sequence]): An iterable (e.g., list, tuple) containing sequences 
                                  (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains an 
                                    element from the input iterable and its length.
    """
    return [(i, len(i)) for i in lst]


