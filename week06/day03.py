import sys

if len(sys.argv) != 2:
    sys.exit("Enter a number")

n = int(sys.argv[1])

if n % 2 == 0:
    print("EVEN")
else:
    print("ODD")