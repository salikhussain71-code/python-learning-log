import sys

# Check number of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

# Print greeting using the argument
print("Hello, my name is", sys.argv[1])
