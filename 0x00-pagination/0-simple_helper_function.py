#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page and page_size.
The function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""


import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    returns in a list for those particular pagination parameters.
    """
    # page - 1 is the current page
    # page_size is the page size to divide the data_set into
    return ((page - 1) * page_size, page * page_size)
