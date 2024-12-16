#!/usr/bin/env python3
""" 9-element_length module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ A function that returns a list where each element
    is a tuple consisting of the list of elements and length
    in integer of the element"""
    return [(i, len(i)) for i in lst]
