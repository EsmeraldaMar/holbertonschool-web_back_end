#!/usr/bin/env python3
""" Takes float multiplier as argument,returns
func which multiplies float by 'multiplier' """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier function"""
    def fn(num: float):
        return num * multiplier
    return fn
