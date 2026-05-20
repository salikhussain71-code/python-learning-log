# Day 05 - Loops (while & for)
# CS50P - Week 2

# 1. while loop — flawed logic (never executes)
i = 3
while i != 3:
    print("meow")
    i = i - 1

# 2. while loop — correct
i = 0
while i < 3:
    print("meow")
    i = i + 1

# 3. while loop — shorthand
i = 0
while i < 3:
    print("meow")
    i += 1

# 4. for loop — list
for i in [0, 1, 2]:
    print("meow")

# 5. for loop — range
for i in range(3):
    print("meow")

# 6. for loop — large range
for i in range(10000):
    print("meow")

# 7. for loop — underscore (unused variable)
for _ in range(3):
    print("meow")

# 8. print with newline and end parameter
print("meow\n" * 3, end="")