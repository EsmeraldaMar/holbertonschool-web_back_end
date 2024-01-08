#!/usr/bin/env python3
""" to_kv function, takes int, str or float
returns tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Complex types - string and int/float to tuple """
    return (k, v * v)
