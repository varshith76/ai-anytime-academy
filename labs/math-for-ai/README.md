# A small maths toolkit

My solution to the **Vectors, similarity and probability** lab at [AI Anytime Academy](https://academy.aianytime.net/learn/math-for-ai).

Implement five functions that turn up again and again in AI — similarity, length, probabilities and loss — in plain Python.

## Requirements

- `dot(a, b)` returns the dot product; mismatched lengths raise `ValueError`
- `norm(v)` returns the Euclidean (L2) length
- `softmax(xs)` returns probabilities that sum to 1 and must not overflow on inputs like `[1000, 1001]`
- `cross_entropy(probs, target)` returns `-log(probs[target])`; a zero probability returns `float('inf')`
- `argmax(xs)` returns the index of the largest value (first one on ties)

Graded: 100% (10 checks, including hidden tests) in an isolated sandbox.
