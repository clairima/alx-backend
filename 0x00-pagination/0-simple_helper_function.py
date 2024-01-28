#!/usr/bin/env python3
"""
definition of index_range function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple[int, int]: Start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
