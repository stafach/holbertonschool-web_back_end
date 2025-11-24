#!/usr/bin/env python3
"""Module that defines a function
to sum a list of mixed integers and floats."""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of mixed integers and floats.

    Args:
        mxd_lst (List[Union[float, int]]): A list of integers and floats.

    Returns:
        float: The sum of all the integers and floats in the list.
    """
    total: float = 0.0
    for item in mxd_lst:
        total += item
    return total
