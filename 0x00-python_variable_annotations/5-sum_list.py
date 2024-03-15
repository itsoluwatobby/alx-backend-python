#!/usr/bin/env python3
"""
a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """
    A function sum_list which takes a list input_list and
    returns a sum of floats
    """
    sum_float = 0
    for num in input_list:
        sum_float += num
    return sum_float
