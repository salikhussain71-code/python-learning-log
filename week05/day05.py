import sys

try:
    print("Hello,", sys.argv[1])
except IndexError:
    print("Missing command-line argument")