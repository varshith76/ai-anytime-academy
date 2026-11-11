# A small toolkit for data programs

My solution to the **Clean, reliable Python** lab at [AI Anytime Academy](https://academy.aianytime.net/learn/python-for-ai).

Build five utilities you'll reuse in later labs — batching, timing, a validated record, conversion to rows and safe text truncation.

## Requirements

- `batched(items, n)` is a generator yielding lists of up to `n` items; `n < 1` raises `ValueError`
- `timed` is a decorator that returns the function's result and stores the last duration in milliseconds on `wrapper.last_ms`
- `Grade(student, score)` is a dataclass; an empty student name or a score outside 0–100 raises `ValueError`
- `to_rows(grades)` returns `[{'student': …, 'score': …}]` dicts in the same order
- `truncate_words(text, max_words)` keeps at most `max_words` words and appends `…` only when it cut something

Graded: 100% (13 checks, including hidden tests) in an isolated sandbox.
