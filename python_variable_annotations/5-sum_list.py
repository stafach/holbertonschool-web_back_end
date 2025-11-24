#!/usr/bin/env python3
"""Module that defines a function to
sum a list of floats with type annotations."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of all the elements of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of all the elements of the list.
    """
    total: float = 0.0
    for num in input_list:
        total += num
    return total
