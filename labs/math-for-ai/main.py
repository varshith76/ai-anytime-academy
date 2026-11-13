# A small maths toolkit
# AI Anytime Academy — Vectors, similarity and probability
# Passed 100% of graded checks on 2026-11-13
# https://academy.aianytime.net/learn/math-for-ai

import math

def dot(a, b):
    """Dot product. Mismatched lengths -> ValueError."""
    if len(a) != len(b):
        raise ValueError(f"Length mismatch: {len(a)} vs {len(b)}")
    total = 0.0
    for x, y in zip(a, b):
        total += x * y
    return total

def norm(v):
    """Euclidean (L2) length: sqrt(sum(x*x))."""
    total = 0.0
    for x in v:
        total += x * x
    return math.sqrt(total)

def softmax(xs):
    """Probabilities that sum to 1. No overflow on [1000, 1001]."""
    if len(xs) == 0:
        raise ValueError("softmax needs at least one value")
    m = max(xs)
    exps = []
    for x in xs:
        exps.append(math.exp(x - m))
    total = sum(exps)
    result = []
    for e in exps:
        result.append(e / total)
    return result

def cross_entropy(probs, target):
    """-log(probs[target]). Zero probability -> float('inf')."""
    p = probs[target]
    if p == 0:
        return float("inf")
    return -math.log(p)

def argmax(xs):
    """Index of largest value. First one wins on ties."""
    if len(xs) == 0:
        raise ValueError("argmax needs at least one value")
    best_index = 0
    best_value = xs[0]
    for i in range(1, len(xs)):
        if xs[i] > best_value:
            best_value = xs[i]
            best_index = i
    return best_index