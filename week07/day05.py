import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:]:
    print("hello, my name is", name)
