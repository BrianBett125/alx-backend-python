#!/usr/bin/env python3
""" 8-make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function make_multiplier that takes a
    float multiplier as argument and returns a function that
    multiplies a float by multiplier"""
    def multiplier_function(x: float) -> float:
        """ multiplies float by a multiplier"""
        return x * multiplier
    return multiplier_function
