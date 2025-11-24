#!/usr/bin/env python3
"""Define a function that takes a string
and a number (int or float) and returns a tuple
with the string and the square of the number as a float."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the number as a float.
    """
    return k, float(v**2)
