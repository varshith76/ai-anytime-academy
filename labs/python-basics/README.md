# Your first gradebook

My solution to the **Python from zero** lab at [AI Anytime Academy](https://academy.aianytime.net/learn/python-basics).

Write five small functions that work with marks and text — the building blocks of every program that handles data.

## Requirements

- `average(scores)` returns the mean of a list of numbers, rounded to 1 decimal place; an empty list returns `0.0`
- `letter_grade(score)` returns `A` for 90+, `B` for 75+, `C` for 60+, `D` for 40+ and `F` below 40
- `top_student(marks)` takes a dict of name → score and returns the name with the highest score (alphabetically first on a tie)
- `passed(marks, cutoff=40)` returns the names that scored at least `cutoff`, sorted alphabetically
- `count_words(text)` returns a dict of lowercase word → how many times it appears, ignoring `. , ! ?`

Graded: 100% (11 checks, including hidden tests) in an isolated sandbox.
