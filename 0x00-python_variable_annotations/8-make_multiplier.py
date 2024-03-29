#!/usr/bin/env python3
from typing import Callable
"""
a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier..
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that returns a function that multiplies a float
    by multiplier
    """
    return lambda multiplier2: multiplier2 * multiplier
