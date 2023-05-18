#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer \
        arguments page and page_size.
The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""


import typing
import csv
from typing import List
import math


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    returns in a list for those particular pagination parameters.
    """
    # page - 1 is the current page
    # page_size is the page size to divide the data_set into
    return ((page - 1) * page_size, page * page_size)


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
        """return the appropriate page of the dataset """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
            return data[start:end]
