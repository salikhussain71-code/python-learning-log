# Simple dictionary - one key maps to one value
students = {
    "Salik": "white house",
    "Shakir": "Laal haweli",
    "Amil": "sultana foundation"
}

# Method 1: Direct access by key
print(students["Salik"])
print(students["Shakir"])
print(students["Amil"])

# Method 2: Loop through keys
for student in students:
    print(student, students[student])

# Method 3: Loop with separator
for student in students:
    print(student, students[student], sep=", ")


# List of dictionaries - each student has multiple fields
students = [
    {"name": "Salik",  "house": "white house",       "patronym": "otter"},
    {"name": "Shakir", "house": "foundation house",   "patronym": "stag"},
    {"name": "Amil",   "house": "laal haweli",        "patronym": "jack russell terrier"},
    {"name": "Faizan",   "house": "sultana house",      "patronym": None}
]

# Basic print
for student in students:
    print(student["name"], student["house"], student["patronym"])

# With separator + handle None gracefully
for student in students:
    patronym = student["patronym"] if student["patronym"] is not None else "no patronym"
    print(student["name"], student["house"], patronym, sep=", ")
