# Day 03 - CS50P | int, float, round, f-strings
# Week 01 | 

# --- INT ---
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)

# --- FLOAT ---
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)

# --- ROUND ---
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(z)

# --- COMMA SEPARATOR (1,000 format) ---
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")