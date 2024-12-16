#!/usr/bin/env python3
""" 100-safe_first module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of lst if there is any, otherwise
    return None"""
    if lst:
        return lst[0]
    else:
        return None
