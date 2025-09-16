# src/analytics.py

from typing import List, Optional


def chunk(lst: List[int], size: int) -> List[List[int]]:
    """Split lst into chunks of length size. Last chunk may be shorter.

    Raise ValueError if size <= 0.
    """
    if size <= 0:
        raise ValueError("size must be positive")

    return [lst[i:i+size] for i in range(0, len(lst), size)]


def running_total(start: int, changes: List[int]) -> List[int]:
    """Return list of running totals after applying each change."""
    result: List[int] = []
    total = start
    for c in changes:
        total += c
        result.append(total)
    return result


def index_of_first_at_least(lst: List[int], threshold: int) -> Optional[int]:
    """Return index of first element >= threshold, else None."""
    for i, val in enumerate(lst):
        if val >= threshold:
            return i
    return None
