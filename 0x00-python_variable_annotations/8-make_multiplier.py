#!/usr/bin/python3
from typing import Callable
"""
a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier..
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    eturns a function that multiplies a float by multiplier.
    """
    return lambda multiplier2: multiplier2 * multiplier
