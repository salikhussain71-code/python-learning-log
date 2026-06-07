# ============================================================
# CS50P | Week 4 - Exceptions | Day 2
# Topic: Repetition with while loop, get_int function, pass
# ============================================================


# ----------------------------
# VERSION 1 — while + else + break
# ----------------------------
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# ----------------------------
# VERSION 2 — break inside try (cleaner)
# ----------------------------
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


# ----------------------------
# VERSION 3 — get_int function with else + return
# ----------------------------
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()


# ----------------------------
# VERSION 4 — return directly from try
# ----------------------------
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()


# ----------------------------
# VERSION 5 — pass instead of print
# ----------------------------
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()


# ----------------------------
# VERSION 6 — prompt as parameter (final)
# ----------------------------
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()