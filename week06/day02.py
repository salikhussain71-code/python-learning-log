import sys

if len(sys.argv) < 2:
    sys.exit("Enter at least one name")

for name in sys.argv[1:]:
    print(f"Hello, {name}")