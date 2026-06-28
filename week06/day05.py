import sys

if len(sys.argv) < 2:
    print("Too few arguments")
else:
    for arg in sys.argv[1:]:
        print("Hello, my name is", arg)