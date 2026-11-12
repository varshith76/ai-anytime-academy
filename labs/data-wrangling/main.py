# Clean a messy lead export
# AI Anytime Academy — Working with messy data
# Passed 100% of graded checks on 2026-11-12
# https://academy.aianytime.net/learn/data-wrangling

import csv
import io
import re
import json
from datetime import datetime, date

def parse_csv(text):
    """CSV text -> list of dicts, whitespace stripped from headers and values."""
    if not text.strip():
        return []
    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)
    reader.fieldnames = [h.strip() if h else h for h in reader.fieldnames]
    result = []
    for row in reader:
        if not any(v and v.strip() for v in row.values() if v is not None):
            continue
        clean_row = {}
        for k, v in row.items():
            key = k.strip() if k else k
            value = v.strip() if isinstance(v, str) else v
            clean_row[key] = value
        result.append(clean_row)
    return result

def parse_amount(s):
    """'₹1,200.50', '1200.5', '$ 99' -> float. Empty -> None."""
    if isinstance(s, (int, float)):
        return float(s)
    if s is None:
        return None
    text = str(s).strip()
    if not text:
        return None
    is_negative = False
    if text.startswith("(") and text.endswith(")"):
        is_negative = True
        text = text[1:-1]
    text = text.replace("Rs.", "").replace("Rs", "").replace("₹", "").replace("$", "").replace("€", "").replace("£", "").replace(",", "").strip()
    text = re.sub(r"[^0-9.\-]", "", text)
    if not text or text in ("-", ".", "-."):
        return None
    value = float(text)
    return -abs(value) if is_negative else value

def parse_date(s):
    """'25/12/2024' or '2024-12-25' -> '2024-12-25'. Anything else -> ValueError."""
    if isinstance(s, datetime):
        return s.date().isoformat()
    if isinstance(s, date):
        return s.isoformat()
    if not isinstance(s, str):
        raise ValueError(f"Invalid date: {s!r}")
    text = s.strip()
    if not text:
        raise ValueError("Invalid date: empty string")
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            dt = datetime.strptime(text, fmt)
            return dt.date().isoformat()
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {s!r}. Expected DD/MM/YYYY or YYYY-MM-DD")

def normalize(record):
    """Lower-case email, parse amount + date, keep other fields."""
    out = dict(record)
    if "email" in out and isinstance(out["email"], str):
        out["email"] = out["email"].strip().lower()
    if "amount" in out:
        out["amount"] = parse_amount(out["amount"])
    if "date" in out:
        out["date"] = parse_date(out["date"])
    return out

def dedupe(records, key):
    """Keep first record for each key value, preserving order."""
    seen = set()
    result = []
    for r in records:
        v = r.get(key)
        if v not in seen:
            seen.add(v)
            result.append(r)
    return result

def to_jsonl(records):
    """One JSON object per line, keys sorted."""
    return "\n".join(json.dumps(r, sort_keys=True) for r in records)

def clean_leads(text):
    """Full pipeline: CSV -> clean -> deduped JSONL."""
    rows = parse_csv(text)
    clean = [normalize(r) for r in rows]
    unique = dedupe(clean, "email")
    return to_jsonl(unique)