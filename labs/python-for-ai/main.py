# A small toolkit for data programs
# AI Anytime Academy — Clean, reliable Python
# Passed 100% of graded checks on 2026-11-11
# https://academy.aianytime.net/learn/python-for-ai

import functools
import time
from dataclasses import dataclass


def batched(items, n):
    """Yield lists of up to n items. n < 1 raises ValueError."""
    if n < 1:
        raise ValueError("n must be at least 1")
    
    batch = []
    for item in items:
        batch.append(item)
        if len(batch) == n:
            yield batch
            batch = []
    if batch:
        yield batch
    


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_ms = (time.perf_counter()-start) * 1000
    wrapper.last_ms = None
    return wrapper
@timed
def slow_sum(n):
    return sum(range(n))
    """Decorator: return func's result; store the last duration (ms) on wrapper.last_ms."""
    


@dataclass
class Grade:
    student: str
    score: int
    # TODO: validate in __post_init__ — empty student or score outside 0–100 raises ValueError
    def __post_init__(self):
        if not self.student:
            raise ValueError("student cannot be empty")
        if self.score < 0 or self.score > 100:
            raise ValueError("score must be between 0 and 100")
    


def to_rows(grades):
    """[Grade, ...] -> [{"student": ..., "score": ...}, ...]"""
    result = []  # 1. Empty box to collect dicts
    
    for g in grades:  # 2. Loop through each Grade
        # 3. For each grade, make a dict
        d = {"student": g.student, "score": g.score}
        result.append(d)  # 4. Put it in box
    
    return result  # 5. Give back the box
        
    


def truncate_words(text, max_words):
    """Keep at most max_words words; append '…' only when something was cut."""
    if max_words < 0:
        raise ValueError("max_words cannot be negative")
    
    words = text.split()
    
    if len(words) <= max_words:
        return " ".join(words)  # FIXED: was return text
    
    if max_words == 0:
        return "…"
    
    return " ".join(words[:max_words]) + "…"
