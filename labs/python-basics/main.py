# Your first gradebook
# AI Anytime Academy — Python from zero
# Passed 100% of graded checks on 2026-11-10
# https://academy.aianytime.net/learn/python-basics

def average(scores):
    """Mean of a list of numbers, rounded to 1 decimal. Empty list -> 0.0"""
    """Average of empty list is zero."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 1)
    pass


def letter_grade(score):
    """A for 90+, B for 75+, C for 60+, D for 40+, otherwise F."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
    pass


def top_student(marks):
    """marks is a dict like {"Asha": 82}. Return the name with the highest score."""
    highest = max(marks.values())
    winners = [name for name, score in marks.items() if score == highest]
    return sorted(winners)[0]

    print(top_student({"Asha": 82, "Ram": 95, "Sai": 90}))
    pass


def passed(marks, cutoff=40):
    """Names that scored at least cutoff, sorted alphabetically."""
    """Return only names where score >= cutoff, sorted alphabetically."""
    result = [name for name, score in marks.items() if score >= cutoff]
    return sorted(result)

# Test it
print(passed({"Asha": 82, "Ram": 95, "Sai": 40, "Anu": 90}, 80))
    


def count_words(text):
    """Lowercase word -> count. Ignore the characters . , ! ?"""
    """Lowercase word -> count. Ignore the characters . , ! ?"""
    
    # Step 1: Clean - Remove punctuation
    for ch in ".,!?":
        text = text.replace(ch, "")
    
    # Step 2: Lowercase
    text = text.lower()
    
    # Step 3: Split into words
    words = text.split()
    
    # Step 4: Count
    result = {}
    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1
    
    return result

# Test it
print(count_words("Hello, hello! World."))
# Output: {'hello': 2, 'world': 1}

print(count_words("I love Python, Python loves me!"))
# Output: {'i': 1, 'love': 1, 'python': 2, 'loves': 1, 'me': 1}
    
    
    
