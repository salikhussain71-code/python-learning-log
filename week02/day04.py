# Week 2 Day 4 - AND operator, Parity, Boolean, Match/Case
# CS50P - Salik

# ─────────────────────────────────────────
# PART 1: GRADES - Version 1 (and operator)
# ─────────────────────────────────────────

score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score <= 90:
    print("Grade B")
elif score >= 70 and score <= 80:
    print("Grade C")
elif score >= 60 and score <= 70:
    print("Grade D")
else:
    print("Grade F")

# ─────────────────────────────────────────
# PART 1: GRADES - Version 2 (chained comparison)
# ─────────────────────────────────────────

score = int(input("Score: "))
if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 90:
    print("Grade B")
elif 70 <= score <= 80:
    print("Grade C")
elif 60 <= score <= 70:
    print("Grade D")
else:
    print("Grade F")

# ─────────────────────────────────────────
# PART 1: GRADES - Version 3 (most concise)
# ─────────────────────────────────────────

score = int(input("Score: "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# ─────────────────────────────────────────
# PART 2: PARITY - Version 1 (simple)
# ─────────────────────────────────────────

x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# ─────────────────────────────────────────
# PART 2: PARITY - Version 2 (with function)
# ─────────────────────────────────────────

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

# ─────────────────────────────────────────
# PART 2: PARITY - Version 3 (ternary)
# ─────────────────────────────────────────

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False

main()

# ─────────────────────────────────────────
# PART 2: PARITY - Version 4 (most concise)
# ─────────────────────────────────────────

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0

main()

# ─────────────────────────────────────────
# PART 3: HOUSES - Version 1 (if/elif)
# ─────────────────────────────────────────

name = input("What's your name? ")
if name == "Salik":
    print("Khan House")
elif name == "Shakir":
    print("White House")
elif name == "Amil":
    print("Monal House")
elif name == "Nasir":
    print("Foundation House")
elif name == "Faizan":
    print("Sultan House")
else:
    print("Who?")

# ─────────────────────────────────────────
# PART 3: HOUSES - Version 2 (or operator)
# ─────────────────────────────────────────

name = input("What's your name? ")
if name == "Salik" or name == "Shakir" or name == "Amil":
    print("Khan House")
elif name == "Faizan":
    print("Sultan House")
else:
    print("Who?")

# ─────────────────────────────────────────
# PART 3: HOUSES - Version 3 (match/case)
# ─────────────────────────────────────────

name = input("What's your name? ")
match name:
    case "Salik":
        print("White House")
    case "Shakir":
        print("Khan House")
    case "Amil":
        print("Beacon House")
    case "Nasir":
        print("Foundation House")
    case _:
        print("Who?")

# ─────────────────────────────────────────
# PART 3: HOUSES - Version 4 (match/case with |)
# ─────────────────────────────────────────

name = input("What's your name? ")
match name:
    case "Salik" | "Shakir" | "Amil":
        print("Khan House")
    case "Nasir":
        print("Foundation House")
    case _:
        print("Who?")