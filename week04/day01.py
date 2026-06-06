# Week 4 - Day 1: Exceptions in Python
# Learned: SyntaxError, ValueError, NameError

# --- Concept 1: SyntaxError ---
# Happens when code structure is wrong.
# Example: missing closing parenthesis causes SyntaxError.

# x = int(input("What's x?")   ← this line has SyntaxError (missing closing paren)


# --- Concept 2: ValueError with try/except ---

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# --- Concept 3: try/except/else (avoids NameError) ---

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
