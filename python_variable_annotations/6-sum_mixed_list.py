#!/usr/bin/env python3
""" takes a list mxd_lst of integers and floats
returns sum as a float."""
from typing import List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ sum_mixed_list function """
    return sum(mxd_lst)
