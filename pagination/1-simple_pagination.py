#!/usr/bin/env python3
""" func that takes two integers as args page & page_size"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ returns a tuple of size two containing start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            pass


def get_page(page: int = 1, page_size: int = 10) -> List[List]:
    """ Takes 2 args, returns empty list 
     if out of range else requested page"""
    assert(type(page) == int and page > 0)
    # checks type f=of arg and checks if it's more than 0
    assert(type(page_size) == int and page_size > 0)
    start, end = index_range(page, page_size)
    pages = []
    if start >= len(self.dataset()):
        return pages
    pages = self.dataset()
    return pages[start:end]
