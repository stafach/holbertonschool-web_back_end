#!/usr/bin/env python3
"""Module that provides a function to create multipliers."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies its input by the given multiplier."""
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
