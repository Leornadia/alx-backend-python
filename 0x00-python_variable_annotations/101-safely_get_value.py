#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""
from typing import Mapping, Any, Union, TypeVar, NoneType

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, NoneType] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to retrieve the value from.
        key (Any): The key to search for in the dictionary.
        default (Union[T, NoneType], optional): The value to return if the key
                                                is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary, or
                       the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
