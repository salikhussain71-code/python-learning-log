import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
else:
    sys.exit("Usage: python say.py NAME")