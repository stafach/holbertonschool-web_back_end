#!/usr/bin/env python3
"""Module that defines a function
to compute the floor of a float number with type annotations."""


def floor(n: float) -> int:
    """Returns the floor of a float number as an integer."""
    if n >= 0 or n == int(n):
        return int(n)
    return int(n) - 1
