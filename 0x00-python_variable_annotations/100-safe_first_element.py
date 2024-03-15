#!/usr/bin/env python3
from typing import Union, Any, Sequence
"""
Augment the following code with the correct duck-typed annotations:
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotate the function with the ccurate the types"""
    if lst:
        return lst[0]
    else:
        return None
