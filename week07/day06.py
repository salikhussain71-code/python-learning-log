import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
else:
    cowsay.cow("hello, world")
