import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"hello, {sys.argv[1]}")
else:
    cowsay.cow("hello, world")