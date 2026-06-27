import sys

if len(sys.argv) != 2:
    sys.exit("Enter a number")

n = int(sys.argv[1])

if n > 0:
    print("POSITIVE")
elif n < 0:
    print("NEGATIVE")
else:
    print("ZERO")