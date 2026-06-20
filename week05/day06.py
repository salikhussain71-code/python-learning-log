import sys

try:
    x = int(sys.argv[1])
    print(f"x is {x}")
except IndexError:
    print("Missing command-line argument")
except ValueError:
    print("Command-line argument is not a number")