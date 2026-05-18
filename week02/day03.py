# Week 2 Day 3 - Conditionals and Boolean Expressions

# 1. Boolean Expressions
# Boolean means yes or no, True or False
# We use them to ask questions in code

# 2. Comparison Operators
# == equal to
# != not equal to
# <  less than
# >  greater than
# <= less than or equal to
# >= greater than or equal to

# --- Example 1: Multiple if statements ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# Tested in terminal with 1 2, 2 1, 1 1

# --- Example 2: Using elif ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# elif is shorter and stops after first true condition

# --- Example 3: Using else ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# else means do this for everything else

# --- Example 4: Using or ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# --- Example 5: Using != ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# != is cleaner than using or

# --- Example 6: Using == ---
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# == checks if two values are exactly equal