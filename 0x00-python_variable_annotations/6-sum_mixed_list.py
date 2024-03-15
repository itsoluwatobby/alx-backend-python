#!/usr/bin/python3
from typing import List, Union
"""
a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list"""
    summed = 0
    for num in mxd_lst:
        summed += num
    return summed
