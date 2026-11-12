# Clean a messy lead export

My solution to the **Working with messy data** lab at [AI Anytime Academy](https://academy.aianytime.net/learn/data-wrangling).

A sales team exported leads from three tools into one CSV. Turn it into clean, de-duplicated JSONL an AI pipeline can trust.

## Requirements

- `parse_csv(text)` returns a list of dicts with whitespace stripped from headers and values
- `parse_amount(s)` turns strings like `₹1,200.50`, `1200.5` or `$ 99` into floats; empty strings become `None`
- `parse_date(s)` converts `DD/MM/YYYY` or `YYYY-MM-DD` to `YYYY-MM-DD`; anything else raises `ValueError`
- `normalize(record)` lower-cases `email`, applies the two parsers to `amount` and `date`, and keeps other fields
- `dedupe(records, key)` keeps the first record for each key value, preserving order
- `to_jsonl(records)` returns one JSON object per line with sorted keys

Graded: 100% (10 checks, including hidden tests) in an isolated sandbox.
