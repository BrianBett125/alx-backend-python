#!/usr/bin/env python3
""" 101-safely_get_value module """
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a dct[key] if it exists,
    otherwise returns `default`"""
    if key in dct:
        return dct[key]
    else:
        return default
