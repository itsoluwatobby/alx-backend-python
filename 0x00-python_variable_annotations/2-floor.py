#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""


def floor(n: float):
    """
    A function that takes in a float n as argument and
    turn the floor of a float
    """
    return int(n) if n >= 0 else int(n) - 1
