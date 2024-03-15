#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union
"""
Given the parameters and the return values, add type annotations
to the function
"""


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Annotate with the correct types and make the
    file executable
    """
    if key in dct:
        return dct[key]
    else:
        return default
