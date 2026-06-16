#Program 1: Using try and except

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")

#Program 2: Using if, elif, and else

import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])