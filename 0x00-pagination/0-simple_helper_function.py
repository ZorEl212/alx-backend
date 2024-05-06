#!/usr/bin/env python
"""Simple helper function for pagenation"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index"""
    return (page - 1) * page_size, page * page_size
