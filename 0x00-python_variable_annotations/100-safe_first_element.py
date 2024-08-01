#!/usr/bin/env python3
"""
This module provides a function to safely return the first element of a list.
"""
from typing import Sequence, Any, Union, NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Return the first element of a list if it exists, otherwise return None.

    Args:
        lst (Sequence[Any]): The input list.

    Returns:
        Union[Any, NoneType]: The first element of the list, or None if the list
                             is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
